# APIs, databases, security & Git — integrated overview

> Reference notes for backend interviews — API design, data stores, auth, and version control in one pass.

---

### At a glance · integrated overview

> *Skim this block first; each numbered section below goes deeper.*

**Focus** — Tell one **end-to-end** story: HTTP → **auth** → service → **DB** → **Git**.

**Connect** — Stateless APIs, **migrations** in repo, **no secrets** in Git, **least-privilege** DB users.

**Sketch** — Client → API → **pool** → DB replica; branch → **PR** → CI.

#### Talk track (~60 s)

APIs expose **versioned** resources with **clear errors** and **auth** (Bearer or session). Data lives in **normalized** tables where relationships matter; **indexes** for hot paths; **schema changes** reviewed like code. **Trunk or GitFlow** with CI on PRs; never commit **`.env`**. Use a **secrets manager** for credentials.

#### Quick checks

- [ ] One diagram: **request → JWT validation → service → DB**.  
- [ ] **Merge vs rebase** — when you’d use each on a shared branch.  
- [ ] **SQL injection** — answer in one line (**parameterized** queries).

---

## 1. APIs

**What an API is**  
Not just an “endpoint” — it is a **contract** between client and server.

**Typical flow**  
`Client → HTTP → Server → Business logic → DB → Response`

**Sample request**

```http
GET /users HTTP/1.1
Host: example.com
Authorization: Bearer <token>
```

**Sample response**

```json
{ "data": [], "status": 200 }
```

### REST principles

| Idea | Notes |
|------|--------|
| Stateless | Server does not rely on server-side session for each request. |
| Resource-based | Paths like `/users`, `/users/{id}`. |
| HTTP methods | GET (read), POST (create), PUT (update), DELETE (remove). |

### Advanced topics

- **Idempotency** — Repeating the same request yields the same outcome (e.g. PUT is idempotent; POST often is not).
- **Pagination** — e.g. `GET /users?page=1&limit=10` to avoid huge payloads.
- **Rate limiting** — Token bucket, fixed window, etc., to limit abuse.
- **Versioning** — e.g. `/v1/users`, `/v2/users`.
- **Caching** — Redis, CDN, etc., to improve latency and load.

---

## 2. Databases

### SQL (relational)

Examples: MySQL, PostgreSQL.

- **Model** — Tables, rows, relationships.
- **Indexes** — Speed lookups; without an index, scans can be **O(n)**; with a suitable index, often **O(log n)**.

### NoSQL

Examples: MongoDB, Redis.

- **Common types** — Document, key-value, graph.

### Internals & design

- **ACID** — Atomicity, consistency, isolation, durability.
- **Transactions** — e.g. `BEGIN` / `UPDATE …` / `COMMIT`.
- **Normalization** — Less redundancy, clearer integrity.
- **Denormalization** — Can improve read performance at the cost of redundancy.

### Scaling

- **Vertical** — Bigger machine.
- **Horizontal** — Sharding, replication.

---

## 3. Security

### JWT (JSON Web Token)

- **Shape** — `header.payload.signature`
- **Flow** — Login → server issues token → client sends it (e.g. `Authorization: Bearer …`).

### OAuth 2.0

- **Idea** — Delegated access (e.g. “Login with Google”).
- **Flow (high level)** — User authenticates with provider → app receives/uses tokens without handling the user’s password.

### SAML

- **Use** — Enterprise SSO.
- **Roles** — Identity Provider (IdP), Service Provider (SP).

### Practices

HTTPS, input validation, rate limiting, token expiry, secure headers.

---

## 4. Git

### What Git does

Tracks project history using **snapshots** (not only line-by-line diffs).

### Core ideas

| Concept | Meaning |
|---------|--------|
| Commit | Snapshot of the tree at a point in time. |
| Branch | Independent line of development. |
| Merge | Combine branch histories. |

### Advanced

- **Rebase** — Replay commits for a linear history (rewrite risk; know when it’s appropriate).
- **Cherry-pick** — Apply a specific commit elsewhere.
- **Stash** — Temporarily shelve working changes.

### Merge vs rebase

| Merge | Rebase |
|--------|--------|
| Preserves full history, merge commits | Cleaner, more linear history |

---

## Summary

- **API** — Exposes behavior and couples clients to a clear contract.  
- **Database** — Persists and serves data; choose SQL vs NoSQL by consistency, shape, and scale.  
- **Security** — JWT, OAuth, SAML address different authZ/authN needs.  
- **Git** — Manages change history and collaboration.

---

## Interview questions (quick list)

**APIs** — How do you design scalable APIs? What is idempotency?

**Databases** — SQL vs NoSQL? Index vs full table scan?

**Security** — JWT vs OAuth? How do you secure APIs?

**Git** — Merge vs rebase? How do you resolve conflicts?
