# REST / API Design Deep Dive & Hard Scenarios (Q&A)

> **Source:** Extracted from `notes/All_chats.md` (Akamai SDE-II prep). Content preserved; reorganized into Concepts vs Interview sections.

**How to read:** Start with **At a glance** / talk track if present, then the full chapter. **Fenced code blocks** are copy-paste examples; **tables** compare options; **ASCII diagrams** use monospace — widen the pane or scroll horizontally.

## Concepts

> *Skim **At a glance** first — a short on-ramp. Below the line is the full chapter.*

---

### At a glance · APIs / REST

- **Frame APIs as contracts:** versioning, **errors**, **pagination**, **idempotency**, **timeouts**, **rate limits**.
- **Tie to ops:** observability (**correlation IDs**), **SLAs**, **backward compatibility**.
- **Scenarios:** double submit, **large payloads**, **partial failure** across downstreams.

#### Talk track (~60 s)

REST maps **resources** to **URLs**; **verbs** imply intent (**GET** safe/idempotent, **PUT** idempotent, **POST** creates). Use **status codes** honestly (**409** conflict, **429** rate limit). **Version** in path or header. **Idempotency-Key** for POST payments. **HATEOAS** rarely required in interviews — focus on **clear schemas**, **validation**, and **problem+json**-style errors.

#### Easy mistakes

- **200** with error body.  
- **Breaking** clients on minor changes — **deprecation** headers / sunset.  
- No story for **retry storms** — **exponential backoff + jitter**.

#### Quick checks

- [ ] **Idempotent POST** — how you’d implement.  
- [ ] **Cursor vs offset** pagination trade-offs.  
- [ ] **401 vs 403** vs **404** for authz.

🌐 PART 1: WHAT AN API REALLY IS (NOT BASIC)
💡 Real Definition
API = contract + abstraction + boundary

🧠 Internally:
Client → HTTP → API Layer → Business Logic → DB → Response
🔥 SDE-2 Insight:
“API is the boundary where performance, security, and scalability decisions are enforced”

⚙️ PART 2: HTTP DEEP DIVE
📦 Request Internals
POST /users HTTP/1.1
Host: example.com
Authorization: Bearer token
Content-Type: application/json
📦 Response
{
  "data": {},
  "error": null
}
💡 Status Codes (YOU Core)
Code	Meaning
200	Success
201	Created
400	Bad request
401	Unauthorized
500	Server error
🧠 PART 3: API DESIGN
🔥 REST Principles
1️⃣ Resource-based
/users
/users/{id}
2️⃣ Stateless
👉 No server-side session

3️⃣ Idempotency
Method	Idempotent
GET	✅
PUT	✅
POST	❌
💣 Advanced Design Concepts
🔥 Pagination
GET /users?page=1&limit=10
🔥 Filtering
GET /users?age=25
🔥 Versioning
/v1/users
/v2/users
⚡ PART 4: API PERFORMANCE
💥 Problem:
API is slow

🔥 Solutions:
1️⃣ Caching
👉 Use Redis

2️⃣ Compression
👉 GZIP response

3️⃣ Pagination
👉 Avoid large payloads

4️⃣ Async Processing
👉 Background jobs

🔐 PART 5: API SECURITY (CRITICAL)
🧠 JWT
Flow:
Login

Server issues token

Client sends token

🧠 OAuth
👉 Delegated access
Example: Login with Google

🧠 SAML
👉 Enterprise SSO

🔥 MUST MENTION:
HTTPS

Input validation

Rate limiting

Token expiration

⚙️ PART 6: API SCALING
💡 Techniques:
🔥 Load Balancer
👉 Distribute traffic

🔥 Horizontal Scaling
👉 Multiple servers

🔥 Rate Limiting
👉 Prevent abuse

🔥 Circuit Breaker
👉 Prevent cascading failure

🧠 PART 7: ERROR HANDLING
❌ Bad:
"Something went wrong"
✅ Good:
{
  "error": {
    "code": 400,
    "message": "Invalid email"
  }
}
🧠 PART 8: REAL INTERVIEW SCENARIOS
💣 SCENARIO 1
👉 “Design a scalable User API”

✅ Answer
“I would design RESTful endpoints with pagination, caching using Redis, authentication via JWT, and deploy behind a load balancer for horizontal scalability.”

💣 SCENARIO 2
👉 “API is slow—what will you do?”

✅ Answer
“I would analyze logs, optimize queries, add caching, and introduce async processing for heavy operations.”

💣 SCENARIO 3
👉 “How to secure APIs?”

✅ Answer
“Use HTTPS, JWT-based authentication, input validation, rate limiting, and proper error handling.”

💣 SCENARIO 4
👉 “How to handle 1M requests/min?”

✅ Answer
“Use load balancing, horizontal scaling, caching, rate limiting, and possibly CDN for static responses.”

💣 SCENARIO 5 (ADVANCED)
👉 “How to ensure API reliability?”

✅ Answer
“Use retries, circuit breakers, monitoring tools, and fallback mechanisms to ensure resilience.”

🧠 PART 9: COMMON MISTAKES
❌ No pagination
❌ Large payloads
❌ No caching
❌ Weak security
❌ Poor error handling

🎯 FINAL MENTAL MODEL
Think like:

API = Performance + Security + Scalability + Design
### Practice
Answer these:

1️⃣ What makes an API scalable?
2️⃣ How do you secure an API?
3️⃣ API is slow—step-by-step fix?

👉 “Deep dive JWT + OAuth + SAML”
👉 “Take full backend mock interview”

## Interview questions, mocks & scenarios

Grill me API scenarios (hard)

Now we’re in API SYSTEM DESIGN GRILLING (HARD MODE)—this is exactly how SDE-2 interviews feel.


Think aloud

Justify with performance + security + trade-offs

Avoid generic answers

💣 SCENARIO 1: HIGH-TRAFFIC FEED API
👉 “Design a GET /feed API for millions of users”

❗ Requirements:
Low latency (<100ms)

Personalized feed

High read traffic

🎯 What you MUST cover:
Caching (very important) → Redis

Pagination strategy

Precompute vs real-time

DB choice

💣 SCENARIO 2: WRITE-HEAVY API
👉 “POST /events → 1M requests/sec”

❗ Requirements:
Extremely high throughput

No data loss

🎯 Expectation:
Queue (Kafka style thinking)

Async processing

DB choice (NoSQL vs SQL)

💣 SCENARIO 3: RATE-LIMITED API
👉 “Limit API to 100 req/min per user”

🎯 You MUST explain:
Where to store counters → Redis

Algorithm:

Token bucket OR sliding window

Distributed system handling

💣 SCENARIO 4: SECURE AUTH API
👉 “POST /login + protected APIs”

🎯 You MUST cover:
JWT flow

Token expiration

Refresh tokens

HTTPS

💣 SCENARIO 5: SLOW API DEBUGGING
👉 “GET /users is taking 2 seconds”

🎯 You MUST say:
Logs

DB query analysis

Index check

Caching

💣 SCENARIO 6: FILE UPLOAD API
👉 “Upload large files (100MB+)”

🎯 Expectation:
Streaming upload

Chunking

Storage (S3-type thinking)

💣 SCENARIO 7: VERSIONING PROBLEM
👉 “You need to change API without breaking clients”

🎯 Expectation:
Versioning (/v1, /v2)

Backward compatibility

💣 SCENARIO 8: IDEMPOTENCY
👉 “Payment API—user clicks twice”

🎯 You MUST explain:
Idempotency key

Prevent duplicate transactions

💣 SCENARIO 9: REAL-TIME API
👉 “Chat application API”

🎯 Expectation:
WebSockets vs REST

Pub/Sub

💣 SCENARIO 10: GLOBAL SCALE API
👉 “Users worldwide (low latency)”

🎯 Expectation:
CDN

Geo-distribution

Edge caching


Break your answer

Push deeper

Turn it into SDE-2 level answer


answer all above


💣 SCENARIO 1: High-Traffic Feed API (GET /feed)
✅ Answer
“For a high-traffic feed API, I would optimize for read-heavy workload:

Use precomputed feeds (fan-out on write) to avoid expensive real-time aggregation

Cache feeds in Redis for low latency (<100ms)

Store persistent data in a NoSQL DB like MongoDB

Use cursor-based pagination instead of offset for scalability

Trade-off:

Higher write cost but significantly faster reads, which aligns with feed-heavy systems.”

💣 SCENARIO 2: Write-Heavy API (1M req/sec)
✅ Answer
“I would decouple ingestion from storage:

API → message queue (Kafka-like) → async consumers

Batch writes into DB (like MongoDB or Cassandra-style systems)

This ensures:

High throughput

Backpressure handling

Trade-off:

Eventual consistency but no data loss with durable queues.”

💣 SCENARIO 3: Rate Limiting API
✅ Answer
“I would use Redis to store request counters:

Key: user_id

Increment per request

Set TTL = 60s

Algorithm:

Sliding window or token bucket

Redis is ideal due to:

Atomic operations

Fast in-memory access

For distributed systems:

Use centralized Redis or consistent hashing.”

💣 SCENARIO 4: Secure Auth API
✅ Answer
“I would implement JWT-based authentication:

User logs in → server issues JWT

Token stored client-side

Sent in Authorization header

Security:

HTTPS enforced

Token expiry

Refresh tokens for session continuity

Trade-off:

Stateless but requires careful token revocation strategy.”

💣 SCENARIO 5: Slow API Debugging
✅ Answer
“I would debug step-by-step:

Check logs and monitoring tools

Analyze DB queries (execution plan, indexes)

Identify bottlenecks (CPU, memory, I/O)

Add caching (Redis)

Optimize queries or add indexes

This systematic approach ensures root cause resolution.”

💣 SCENARIO 6: File Upload API (100MB+)
✅ Answer
“I would avoid loading full file in memory:

Use streaming upload

Break into chunks

Upload directly to object storage (S3-like)

Benefits:

Reduced memory usage

Better reliability

Trade-off:

Slight complexity in chunk management.”

💣 SCENARIO 7: API Versioning
✅ Answer
“I would use versioning to avoid breaking clients:

URI versioning: /v1/users, /v2/users

Maintain backward compatibility

Trade-off:

Code duplication vs stability

Over time, deprecate old versions gradually.”

💣 SCENARIO 8: Idempotency (Payments)
✅ Answer
“I would use idempotency keys:

Client sends unique key per request

Server stores key + response

Duplicate request → return same response

This prevents double payments even if user retries.”

💣 SCENARIO 9: Real-Time Chat API
✅ Answer
“REST is not ideal for real-time systems:

Use WebSockets for persistent connection

Use Pub/Sub for message distribution

Backend:

Redis Pub/Sub or Kafka-style system

Trade-off:

More complex but real-time communication enabled.”

💣 SCENARIO 10: Global Scale API
✅ Answer
“For global users:

Use CDN for static content

Geo-distributed servers

Edge caching

Dynamic APIs:

Route to nearest region

Trade-off:

Data consistency vs latency

Use eventual consistency for non-critical data.”

🧠 WHAT INTERVIEWER IS REALLY TESTING
They want to see:

Can you break down problems

Do you know trade-offs

Can you design real systems

🎯 FINAL LEVEL
👉 Your answers should always follow:

Problem → Approach → Tech choice → Trade-off

Now choose:

👉 “Final full mock interview (all rounds)” 😈🔥
👉 “Deep dive security (JWT, OAuth, SAML)”
👉 “Revise everything in 1-page cheat sheet”
