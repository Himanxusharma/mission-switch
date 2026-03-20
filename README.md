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
| **`dsa/`** | **Data structures & algorithms** |
| **`docs/`** | [Study guide](docs/STUDY_GUIDE.md), [question cheatsheet](docs/interview-questions-cheatsheet.md), [introduction](docs/introduction.md) |

**Source chat export:** place **`All_chats.md`** next to these folders **or** under **`notes/All_chats.md`** if you use a `notes/` wrapper — see `scripts/note_paths.py`.

## Pipeline

```bash
python3 scripts/split_all_chats.py
python3 scripts/clean_topic_markdown.py
python3 scripts/refine_topic_voice.py
```

- **Split** regenerates markdown from `All_chats.md` line ranges (does **not** overwrite `backend/apis-db-security-git-overview.md`).
- **Clean / refine** walk all six folders (see `scripts/note_paths.py`).

**Hand-maintained:** `backend/apis-db-security-git-overview.md`.
