#!/usr/bin/env python3
"""
Lightweight readability pass for topic notes (same family as payments-microservices polish):

1. After the standard **Source:** blockquote, insert a short **How to read** paragraph
   (once per file, idempotent).
2. Wrap contiguous ASCII box-drawing blocks (lines containing ┌/│/└ etc.) in ```text fences,
   skipping content already inside markdown code fences.

Run from repo root:
  python3 scripts/enhance_topic_readability.py
  python3 scripts/enhance_topic_readability.py --dry-run
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

TOPIC_GLOBS = [
    "foundation/*.md",
    "backend/*.md",
    "architecture/*.md",
    "platform/*.md",
    "career/*.md",
    "dsa/*.md",
]

SKIP_NAMES = {"README.md"}

READER_BLURB = (
    "\n**How to read:** Start with **At a glance** / talk track if present, then the full chapter. "
    "**Fenced code blocks** are copy-paste examples; **tables** compare options; "
    "**ASCII diagrams** use monospace — widen the pane or scroll horizontally.\n"
)

SOURCE_LINE = "> **Source:**"
READER_MARKER = "**How to read:**"


def topic_markdown_files() -> list[Path]:
    out: list[Path] = []
    for g in TOPIC_GLOBS:
        out.extend(sorted(REPO.glob(g)))
    return [p for p in out if p.name not in SKIP_NAMES]


def insert_reader_blurb(text: str) -> tuple[str, bool]:
    head = text[:6000]
    if READER_MARKER in head or "**How this file is laid out:**" in head:
        return text, False
    if SOURCE_LINE not in text[:4000]:
        return text, False
    # Insert immediately after the first Source blockquote line (single-line quote).
    lines = text.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if line.startswith(SOURCE_LINE):
            # If next non-empty line is already our blurb, skip
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            if j < len(lines) and READER_MARKER in lines[j]:
                return text, False
            lines.insert(i + 1, READER_BLURB)
            return "".join(lines), True
    return text, False


BOX_CHARS = frozenset("│┌┐└┘├┤┬┴┼─▼▲")


def _has_box_drawing(line: str) -> bool:
    return any(c in BOX_CHARS for c in line)


# Lines that end an ASCII diagram block (prose starts below)
_STOP_LINE = re.compile(
    r"^(Highlights|Flow|Interview Key Points|Detailed Components)\s*:\s*$",
    re.IGNORECASE,
)


def _is_section_emoji_line(line: str) -> bool:
    s = line.lstrip()
    return bool(re.match(r"^\d+\s*[️⃣]", s)) or bool(re.match(r"^[0-9]+️⃣", s))


def wrap_ascii_blocks(text: str) -> tuple[str, int]:
    """Wrap box-drawing runs in ```text fences. Returns (new_text, num_wrapped)."""
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    in_fence = False
    fence_marker = ""
    wrapped = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            in_fence = not in_fence
            if in_fence:
                fence_marker = stripped[3:].strip()
            out.append(line)
            i += 1
            continue

        if in_fence:
            out.append(line)
            i += 1
            continue

        # Start a diagram only on a top box line (┌) to avoid false positives
        if "┌" in line:
            start = i
            i += 1
            while i < len(lines):
                L = lines[i]
                st = L.strip()
                if st.startswith("```"):
                    break
                if _STOP_LINE.match(L.rstrip("\n")):
                    break
                # Next numbered system section (e.g. "2️⃣ Chat") — end diagram
                if _is_section_emoji_line(L) and i > start + 2:
                    break
                if _has_box_drawing(L) or (L.strip() == "" and i + 1 < len(lines) and _has_box_drawing(lines[i + 1])):
                    i += 1
                    continue
                # Prose line without box drawing ends the block
                if L.strip() and not _has_box_drawing(L):
                    break
                i += 1

            block = lines[start:i]
            if len(block) >= 3:
                out.append("```text\n")
                out.extend(block)
                if not out[-1].endswith("\n"):
                    out[-1] += "\n"
                out.append("```\n\n")
                wrapped += 1
                continue

        out.append(line)
        i += 1

    return "".join(out), wrapped


def process_file(path: Path, dry_run: bool) -> tuple[bool, bool, int]:
    """Returns (reader_added, changed, ascii_wrapped)."""
    raw = path.read_text(encoding="utf-8")
    text, reader_added = insert_reader_blurb(raw)
    text2, n_wrap = wrap_ascii_blocks(text)
    changed = reader_added or n_wrap > 0
    if changed and not dry_run:
        path.write_text(text2, encoding="utf-8")
    return reader_added, changed, n_wrap


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="Print actions only")
    args = ap.parse_args()
    files = topic_markdown_files()
    total_reader = 0
    total_wrap = 0
    for p in files:
        ra, ch, nw = process_file(p, args.dry_run)
        if ch:
            print(f"{p.relative_to(REPO)}: reader={ra} ascii_blocks={nw}")
            if ra:
                total_reader += 1
            total_wrap += nw
    print(f"Done. Files with changes: scanned {len(files)}; reader blurbs added: {total_reader}; ASCII blocks wrapped: {total_wrap}")


if __name__ == "__main__":
    main()
