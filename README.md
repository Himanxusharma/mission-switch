# mission-switch

*Interview prep notes — short on-ramps first, depth when you’re ready.*

Backend + system design + DSA (Akamai SE II–style), organized in **six folders** plus **`docs/`**.

**How to read:** [docs/READING.md](docs/READING.md) · **Order & regen:** [docs/STUDY_GUIDE.md](docs/STUDY_GUIDE.md)

## Layout

| Path | Contents |
|------|----------|
| **`foundation/`** | JD / interview overview, **Java**, **OOP** |
| **`backend/`** | Spring, Node/Spring internals, **DBs**, REST, **auth**, **Kafka**, hand-maintained **APIs + DB + Git** overview |
| **`architecture/`** | **System design**, **payments / microservices** |
| **`platform/`** | **CI/CD**, Docker/K8s, **cloud**, **Linux**, **monitoring** |
| **`career/`** | **Behavioral** prep, **master index** / big question bank |
| **`dsa/`** | **Data structures & algorithms** — [on-ramp](dsa/README.md), main file [`dsa-patterns-and-practice.md`](dsa/dsa-patterns-and-practice.md) |
| **`docs/`** | [Study guide](docs/STUDY_GUIDE.md), [question cheatsheet](docs/interview-questions-cheatsheet.md), [introduction](docs/introduction.md) |

**Source chat export:** put **`All_chats.md`** next to these topic folders **or** under **`notes/All_chats.md`**. Exact layout and which files scripts skip are spelled out in [STUDY_GUIDE.md](docs/STUDY_GUIDE.md).

## Pipeline

Regeneration uses small Python helpers under **`scripts/`** (see the study guide if your checkout does not include them yet):

```bash
python3 scripts/split_all_chats.py
python3 scripts/clean_topic_markdown.py
python3 scripts/refine_topic_voice.py
python3 scripts/beautify_playbook_sections.py   # optional: normalize “At a glance” blocks after a split
python3 scripts/enhance_topic_readability.py    # optional: reader blurb + wrap ASCII in ```text```
```

- **Split** — writes topic markdown from **`All_chats.md`** line ranges; does **not** overwrite **`backend/apis-db-security-git-overview.md`**.
- **Clean / refine** — walk all six folders; skip **`README.md`** and the hand-maintained overview **by filename**.
- **Beautify** — reapplies the calm on-ramp headings; safe to re-run after regenerating.

**Hand-maintained:** `backend/apis-db-security-git-overview.md`.
