# Study guide

> *Notes are grouped in six folders. Each file opens with a short **At a glance** strip, then the full chapter — read in two passes if you like.*

Split notes live in **`foundation/`**, **`backend/`**, **`architecture/`**, **`platform/`**, **`career/`**, and **`dsa/`** at the **repo root** (or under **`notes/`** if you use that layout). Source export: **`All_chats.md`**.

**Reading rhythm:** [READING.md](./READING.md) · **Quick questions:** [interview-questions-cheatsheet.md](./interview-questions-cheatsheet.md)

## Suggested reading order (JD-aligned)

| Order | Folder | File | What it covers |
|------:|:------:|------|----------------|
| 1 | foundation | [`interview-overview-and-jd.md`](../foundation/interview-overview-and-jd.md) | JD, rounds, prep strategy |
| 2 | foundation | [`oops.md`](../foundation/oops.md) | OOP, patterns prompts |
| 3 | foundation | [`java.md`](../foundation/java.md) | JVM, collections, concurrency |
| 4 | backend | [`spring-boot-and-apis.md`](../backend/spring-boot-and-apis.md) | Spring Boot, REST, security intro |
| 5 | backend | [`nodejs-and-spring-internals.md`](../backend/nodejs-and-spring-internals.md) | Event loop vs Spring |
| 6 | architecture | [`system-design.md`](../architecture/system-design.md) | SD framework, five systems |
| 7 | dsa | [`dsa-patterns-and-practice.md`](../dsa/dsa-patterns-and-practice.md) | DSA patterns & drills |
| 8 | backend | [`databases-sql-nosql.md`](../backend/databases-sql-nosql.md) | SQL/NoSQL, transactions |
| 9 | backend | [`apis-db-security-git-overview.md`](../backend/apis-db-security-git-overview.md) | APIs + DB + security + **Git** (hand-maintained) |
| 10 | backend | [`apis-rest-advanced-scenarios.md`](../backend/apis-rest-advanced-scenarios.md) | REST deep dive |
| 11 | backend | [`authentication-oauth-saml-jwt.md`](../backend/authentication-oauth-saml-jwt.md) | JWT, OAuth, SAML |
| 12 | backend | [`kafka-event-driven.md`](../backend/kafka-event-driven.md) | Kafka |
| 13 | platform | [`cicd-docker-kubernetes-devops.md`](../platform/cicd-docker-kubernetes-devops.md) | CI/CD, K8s |
| 14 | platform | [`monitoring-observability-elk.md`](../platform/monitoring-observability-elk.md) | Observability |
| 15 | platform | [`cloud-aws-gcp.md`](../platform/cloud-aws-gcp.md) | AWS & GCP |
| 16 | platform | [`linux-windows-administration.md`](../platform/linux-windows-administration.md) | Linux / ops |
| 17 | career | [`behavioral-and-soft-skills.md`](../career/behavioral-and-soft-skills.md) | Behavioral |
| 18 | architecture | [`payments-microservices-architecture.md`](../architecture/payments-microservices-architecture.md) | Microservices, payments Q&A |
| 19 | career | [`topics-master-index.md`](../career/topics-master-index.md) | Master checklist + big bank |

## Regenerating files

```bash
python3 scripts/split_all_chats.py
python3 scripts/clean_topic_markdown.py
python3 scripts/refine_topic_voice.py
python3 scripts/beautify_playbook_sections.py   # optional: normalize “At a glance” blocks after a split
```

- **`split_all_chats.py`** — writes **18** files from **`All_chats.md`**; skips **`backend/apis-db-security-git-overview.md`**.
- **Clean / refine** — all six folders; skip **`README.md`** and the hand-maintained overview **by filename**.
- **`beautify_playbook_sections.py`** — reapplies the calm on-ramp headings after regenerating (safe to run anytime).

Edit line ranges in `scripts/split_all_chats.py` when you append to **`All_chats.md`**.
