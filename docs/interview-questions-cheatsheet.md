# Interview questions — rapid review

> *Answer **out loud** first. Open a link only when you want the full explanation — this page is a map, not the territory.*

**Coverage:** Foundation (Java, OOP) · Backend · Architecture · Platform · DSA · Career · Cross-cutting

---

## Foundation — Java & runtime

| Question | Drill |
|----------|--------|
| Stack vs heap; when do you get `StackOverflowError` vs `OutOfMemoryError`? | [java.md](../foundation/java.md) |
| Why is `String` immutable? `String` vs `StringBuilder` vs `StringBuffer`? | [java.md](../foundation/java.md) |
| `==` vs `equals()` — when would you still get surprises with `Integer`, `String` interning? | [java.md](../foundation/java.md) |
| How does `HashMap` work internally (buckets, hash, collisions, resize)? | [java.md](../foundation/java.md) |
| `HashMap` vs `ConcurrentHashMap` — locking, use cases? | [java.md](../foundation/java.md) |
| `synchronized`, `volatile`, visibility, deadlock — explain with a concrete API example | [java.md](../foundation/java.md) |

## Foundation — OOP

| Question | Drill |
|----------|--------|
| Four pillars with a **non-toy** example (e.g. payments, auth) | [oops.md](../foundation/oops.md) |
| Abstract class vs interface — when each? Java 8+ default methods? | [oops.md](../foundation/oops.md) |
| Composition vs inheritance — when inheritance hurts | [oops.md](../foundation/oops.md) |
| Name 2–3 patterns you’ve actually used (not just definitions) | [oops.md](../foundation/oops.md) |

## Backend — Spring & APIs

| Question | Drill |
|----------|--------|
| IoC vs DI; what problem does Spring solve in a servlet app? | [spring-boot-and-apis.md](../backend/spring-boot-and-apis.md) |
| `@Component` / `@Service` / `@Repository` — stereotypes and testability | [spring-boot-and-apis.md](../backend/spring-boot-and-apis.md) |
| REST: idempotency for GET/PUT/DELETE/POST; common status codes | [apis-rest-advanced-scenarios.md](../backend/apis-rest-advanced-scenarios.md) |
| Versioning strategies; breaking vs non-breaking changes | [apis-rest-advanced-scenarios.md](../backend/apis-rest-advanced-scenarios.md) |
| Rate limiting, throttling, timeouts, retries — where they live | [apis-rest-advanced-scenarios.md](../backend/apis-rest-advanced-scenarios.md) |

## Backend — Data & messaging

| Question | Drill |
|----------|--------|
| SQL vs NoSQL — pick for orders vs catalog vs sessions | [databases-sql-nosql.md](../backend/databases-sql-nosql.md) |
| Indexes: clustered vs non-clustered; when does an index hurt? | [databases-sql-nosql.md](../backend/databases-sql-nosql.md) |
| Isolation levels; phantom read vs non-repeatable read | [databases-sql-nosql.md](../backend/databases-sql-nosql.md) |
| Kafka: partitions, consumer groups, at-least-once vs exactly-once (trade-offs) | [kafka-event-driven.md](../backend/kafka-event-driven.md) |

## Backend — Security & auth

| Question | Drill |
|----------|--------|
| JWT structure; where to store; refresh rotation; logout story | [authentication-oauth-saml-jwt.md](../backend/authentication-oauth-saml-jwt.md) |
| OAuth2 roles (resource owner, client, authorization server, resource server) | [authentication-oauth-saml-jwt.md](../backend/authentication-oauth-saml-jwt.md) |
| SAML vs OAuth — when enterprises pick SAML | [authentication-oauth-saml-jwt.md](../backend/authentication-oauth-saml-jwt.md) |

## Backend — Node vs Spring (threading & I/O)

| Question | Drill |
|----------|--------|
| Event loop vs thread-per-request; when Node blocks | [nodejs-and-spring-internals.md](../backend/nodejs-and-spring-internals.md) |
| How `DispatcherServlet` fits the request path | [nodejs-and-spring-internals.md](../backend/nodejs-and-spring-internals.md) |

## Architecture — system design

| Question | Drill |
|----------|--------|
| Clarify functional + non-functional requirements before drawing boxes | [system-design.md](../architecture/system-design.md) |
| Design URL shortener / chat / notifications — data model + cache + scale | [system-design.md](../architecture/system-design.md) |
| API vs microservice vs batch job vs cron — who owns what | [payments-microservices-architecture.md](../architecture/payments-microservices-architecture.md) |
| Payment flow: idempotency, double charge, reconciliation hooks | [payments-microservices-architecture.md](../architecture/payments-microservices-architecture.md) |

## Platform — ship & operate

| Question | Drill |
|----------|--------|
| Rolling vs blue-green vs canary — risk and rollback | [cicd-docker-kubernetes-devops.md](../platform/cicd-docker-kubernetes-devops.md) |
| Docker image vs container; multi-stage builds (why) | [cicd-docker-kubernetes-devops.md](../platform/cicd-docker-kubernetes-devops.md) |
| Pod / Deployment / Service / Ingress — one-sentence each | [cicd-docker-kubernetes-devops.md](../platform/cicd-docker-kubernetes-devops.md) |
| Metrics vs logs vs traces; what you’d check for a latency spike | [monitoring-observability-elk.md](../platform/monitoring-observability-elk.md) |
| EC2 vs Lambda vs ECS/EKS — rough decision | [cloud-aws-gcp.md](../platform/cloud-aws-gcp.md) |
| `journalctl`, disk full, port in use — how you triage | [linux-windows-administration.md](../platform/linux-windows-administration.md) |

## DSA (screening / round 1)

| Question | Drill |
|----------|--------|
| Two Sum → how HashMap buys O(n) | [dsa-patterns-and-practice.md](../dsa/dsa-patterns-and-practice.md) |
| Sliding window template — when it applies | [dsa-patterns-and-practice.md](../dsa/dsa-patterns-and-practice.md) |
| BFS vs DFS — graph + tree use cases | [dsa-patterns-and-practice.md](../dsa/dsa-patterns-and-practice.md) |
| LRU — HashMap + doubly linked list story | [dsa-patterns-and-practice.md](../dsa/dsa-patterns-and-practice.md) |

## Career — behavioral & narrative

| Question | Drill |
|----------|--------|
| “Tell me about yourself” in ~60s — role, stack, impact metric | [behavioral-and-soft-skills.md](../career/behavioral-and-soft-skills.md) |
| One production incident: detection → mitigation → prevention | [behavioral-and-soft-skills.md](../career/behavioral-and-soft-skills.md) |
| Conflict or pushback — STAR, no villain | [behavioral-and-soft-skills.md](../career/behavioral-and-soft-skills.md) |

## Cross-cutting (integrated)

| Question | Drill |
|----------|--------|
| Draw API → auth → service → DB → cache → queue for a flow you know | [apis-db-security-git-overview.md](../backend/apis-db-security-git-overview.md) |
| Git: merge vs rebase; when `rebase` is a bad idea on shared branches | [apis-db-security-git-overview.md](../backend/apis-db-security-git-overview.md) |

---

## Bigger banks (already in repo)

- **Topic checklist + long question lists:** [topics-master-index.md](../career/topics-master-index.md)  
- **JD + round expectations:** [interview-overview-and-jd.md](../foundation/interview-overview-and-jd.md)  
- **Reading order:** [STUDY_GUIDE.md](./STUDY_GUIDE.md)

**Tip:** Pick **3 questions per day** from different sections and record 2-minute voice answers.
