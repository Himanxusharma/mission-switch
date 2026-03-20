# Master Topic Index & Roadmap Summary

> **Source:** Extracted from `notes/All_chats.md` (Akamai SDE-II prep). Content preserved; reorganized into Concepts vs Interview sections.

**How to read:** Start with **At a glance** / talk track if present, then the full chapter. **Fenced code blocks** are copy-paste examples; **tables** compare options; **ASCII diagrams** use monospace — widen the pane or scroll horizontally.

## Concepts

> *Skim **At a glance** first — a short on-ramp. Below the line is the full chapter.*

---

### At a glance · master index

- **This file** is a **map**, not something to memorize in one sitting. Use it to **spot gaps** and jump to the matching folder (`foundation/`, `backend/`, `architecture/`, `platform/`, `career/`, `dsa/`).
- **Weekly:** pick **one weak column** (e.g. Kafka, OAuth, Linux) and schedule **2 hours** + **10 verbal** Q&A from that section.
- **Cross-link:** pair **topics-master-index** with [`docs/interview-questions-cheatsheet.md`](../docs/interview-questions-cheatsheet.md) for a shorter daily pass.

#### Quick checks

- [ ] Skim **one** topic block below you haven’t touched in 2 weeks.  
- [ ] Run **5** random questions **out loud** from the question bank section later in this file.  
- [ ] Sleep — breadth matters only if you can **think under pressure**.

📋 FULL TOPICS COVERED
1️⃣ DSA & Problem Solving
Arrays, Strings, Linked List, Stack, Queue

Trees & Graphs

Dynamic Programming

Sliding Window / Two Pointer / Hashing

Recursion & Backtracking

Sorting & Searching

Hashmaps / Sets

Pattern-based problem solving (25 patterns deep dive)

Internal workings of patterns (how they actually execute in memory)

Interview-grade hard scenarios

2️⃣ OOP & Design Patterns
SOLID principles

Encapsulation, Inheritance, Polymorphism, Abstraction

Design Patterns:

Singleton, Factory, Builder, Strategy, Observer, Adapter, Decorator, Proxy, Composite, Facade

Deep internal workings and use-cases

Real-world SDE-2 interview scenarios

3️⃣ Java & Spring Boot
Java fundamentals (collections, streams, concurrency)

Spring Core: DI, Beans, ApplicationContext

Spring Boot: Auto-configuration, Starter dependencies

REST API development

Authentication & Authorization (OAuth2, SAML, JWT)

Exception handling, validation, logging

Real-world Spring Boot design & best practices

Mock interviews and scenario-based grilling

4️⃣ Node.js
Event loop, Async/await, Promises

Express.js: routing, middleware

REST API design

Database integrations (MongoDB, SQL)

Security best practices

Authentication patterns (JWT, OAuth2)

Real-world Node microservice patterns

5️⃣ Databases
SQL vs NoSQL

Oracle, Snowflake, MongoDB, Redis

Transactions & Isolation Levels

Indexing & Query Optimization

ACID vs BASE

When to use which DB in real-world scenarios

Hard interview scenarios (multi-database architectures, scaling, high availability)

6️⃣ APIs & Web Services
REST APIs, SOAP APIs

API design best practices

Authentication & Authorization (SAML, OAuth, JWT)

Rate-limiting, throttling

API versioning, error handling

Distributed API debugging and scaling

7️⃣ Version Control
Git basics: clone, commit, push, branch

Git workflows: GitFlow, feature branching

Merge, rebase, conflicts

Advanced Git commands for SDE-2

Collaboration & PR review strategies

8️⃣ DevOps & CI/CD
CI/CD pipelines concepts

Jenkins, GitHub Actions concepts

Deployment strategies (rolling, blue-green, canary)

Docker: images, containers, Dockerfile

Kubernetes: Pods, Deployments, Services, StatefulSets

Cluster internals: Control Plane, Node components

Auto-scaling, health checks, self-healing

Real-world troubleshooting scenarios

9️⃣ Monitoring & Observability
Metrics, logs, traces

Tools:

Nagios, New Relic, Splunk, Elasticsearch (ELK)

Alerts, dashboards, distributed system monitoring

Real-world debugging

Log aggregation, inverted index (Elasticsearch internals)

Observability in microservices

10️⃣ Cloud Platforms
Cloud concepts: IaaS, PaaS, SaaS

AWS Deep Dive:

EC2, Lambda, ECS, EKS

S3, EBS, RDS

VPC, Load Balancers, CloudFront

IAM, CloudWatch, Security

GCP Deep Dive:

Compute Engine, Cloud Functions, GKE

Cloud Storage, Persistent Disk, BigQuery

VPC, Load Balancing, CDN

IAM, Stackdriver

Cloud architecture: multi-region, high availability, fault tolerance

Cloud scaling & cost optimization

Event-driven & serverless architectures

11️⃣ Security & Authentication
SAML, OAuth2, JWT

Single Sign-On (SSO) flow

Role-based access control

Token validation & refresh

Best practices for API security

12️⃣ Linux & Windows Administration
Basic commands

File system, processes, users

Permissions, services, package management

Networking, ports, firewall rules

Logs & troubleshooting

13️⃣ Advanced System Design
Backend system design

Microservices architecture

Horizontal scaling

Caching strategies

Database sharding & replication

Load balancing & CDN strategies

Observability integration

🎯 SUMMARY
We have covered everything from low-level coding & DSA → OOP → backend frameworks → databases → API → DevOps → monitoring → cloud → system design.


🎯 Master Roadmap & Mock Interview Question Bank
1️⃣ Data Structures & Algorithms (DSA)
Key Concepts to Master

Arrays & Strings (sliding window, two pointers)

HashMaps & HashSets

Linked Lists (single, double, cycle detection)

Stacks & Queues

Heaps / Priority Queues

Trees & Binary Search Trees

Tries

Graphs (BFS, DFS, Dijkstra, Topological sort)

Dynamic Programming (DP)

Backtracking

Bit Manipulation

Sliding Window

Two Pointers

Prefix Sum

Union-Find

Segment Trees / Fenwick Trees

Greedy Algorithms

Sorting Algorithms (Merge, Quick, Heap)

Searching Algorithms (Binary, Interpolation)

Recursion

Memoization & Tabulation

Top K Problems

LRU / Cache Design Patterns

Matrix problems

Heap + Sliding Window combined problems

Sample Interview Questions

Design a LRU cache from scratch (O(1) get & put).

Find the shortest path in a weighted graph with Dijkstra.

Maximum sum subarray with size k.

Longest substring without repeating characters.

Implement a trie for prefix search.

2️⃣ Databases
Topics

SQL vs NoSQL

Transactions & Isolation Levels (READ COMMITTED, REPEATABLE READ, SERIALIZABLE)

Indexing & Optimization

Sharding & Replication

Caching strategies (Redis / Memcached)

DB choices:

Oracle: Best for transactions & strong consistency

Snowflake: Analytics & reporting

MongoDB: Flexible schema, real-time apps

Redis: In-memory cache, fast lookups

Interview Questions

Explain ACID vs BASE with examples.

How would you scale a transactional DB for high writes?

Difference between vertical & horizontal scaling.

How to design indexes for fast search?

Use cases of NoSQL vs SQL in microservices.

3️⃣ APIs & Backend
Topics

REST vs GraphQL

API versioning

Pagination & filtering

Error handling & retries

Rate limiting

Auth & AuthZ: OAuth2, SAML, JWT, SSO

Real-time APIs: WebSocket, MQTT

API Gateway & Load Balancing

Interview Questions

Design a rate-limited REST API.

How would you handle idempotency in payment APIs?

Explain OAuth2 flow and refresh tokens.

How to handle millions of concurrent connections in WebSocket?

4️⃣ CI/CD & DevOps
Topics

Git workflows (feature branch, PRs, rebase)

CI/CD pipelines

Docker & Kubernetes

Blue/Green & Canary deployments

Infrastructure as Code (Terraform, CloudFormation)

Monitoring & Logging (Prometheus, ELK, New Relic)

Queues for async processing (Kafka, SQS, Pub/Sub)

Interview Questions

Explain canary deployment vs rolling update.

How would you debug a failed CI/CD pipeline?

How to scale Kubernetes pods for variable load?

Monitoring strategy for a microservices system.

5️⃣ Cloud Platforms
Topics

AWS: EC2, S3, RDS, DynamoDB, Lambda, CloudFront, Route53

GCP: GKE, Cloud SQL, Firestore, Cloud Run, Memorystore

Multi-region deployment

CDN & caching

Auto-scaling & fault tolerance

Interview Questions

How would you design a globally available system?

Difference between serverless and containerized deployments.

How to handle storage at petabyte scale?

Cloud cost optimization strategies.

6️⃣ Security & Auth
Topics

OAuth2, SAML, JWT, SSO

TLS / HTTPS, encryption at rest

Rate-limiting & throttling

Data validation & sanitation

DRM for streaming

Interview Questions

Explain SSO with SAML step by step.

Difference between JWT and OAuth2.

How to prevent abuse on high-frequency endpoints?

Secure design for payment processing system.

7️⃣ Microservices & System Design (From 5 Systems)
Systems Covered

URL Shortener → caching, DB, scaling, CDN

Chat Application → WebSocket, DB sharding, pub/sub

E-Commerce → transactions, caching, event-driven

Video Streaming → CDN, transcoding, adaptive bitrate

Job Portal → search, recommendation, messaging, analytics

Interview Questions

How would you scale each system for millions of users?

How to design DB sharding for chat/messages/orders?

How to implement recommendations asynchronously?

How to handle failover in multi-region deployment?

Explain caching strategy for each system.

8️⃣ Monitoring & Observability
Topics

ELK (ElasticSearch, Logstash, Kibana)

Prometheus & Grafana

New Relic / CloudWatch

Logging & alerting strategies

Performance metrics & dashboards

Interview Questions

How to detect and resolve a slow API in production?

How to monitor real-time message delivery latency?

Alert thresholds for critical services.

9️⃣ Mock Interview Strategy
Step-by-Step Daily Grind

Pick 1 topic (DSA, DB, APIs, Cloud, etc.)

Solve 1–2 tough problems / scenario questions.

Discuss real-world trade-offs and optimizations.

Review system design for 1 system → scale, caching, security, CI/CD.

Repeat until all 5 systems are covered.

Mix hard grilling scenarios for SDE-2 level.

I can also prepare a detailed “Day-wise 30-day interview prep schedule” for you with:

DSA + System design + DB + API + Cloud + CI/CD + Security

Mock questions + key points + solution hints

This will let you cover everything for Akamai SDE-2 prep systematically.


## Interview questions, mocks & scenarios

Mock questions + key points + solution hints


🛠️ SDE-2 Mock Interview Question Bank
1️⃣ Data Structures & Algorithms (DSA)
Question	Key Points	Solution Hints
Design an LRU Cache	HashMap + Doubly Linked List	O(1) get & put; maintain order with linked list
Shortest Path in Weighted Graph	Dijkstra / BFS (for unweighted)	PriorityQueue for min distance, adjacency list
Longest Substring Without Repeating Characters	Sliding window + HashSet	Expand window, remove duplicates, track max length
Maximum Sum Subarray of Size K	Sliding window	Maintain running sum, slide window
Implement Trie	Tree nodes, children map	Insert/search prefix, O(L) time
Detect cycle in Linked List	Fast & slow pointers	Return true if fast == slow
Top K Frequent Elements	HashMap + Min Heap	Count frequencies, heap of size K
Merge Intervals	Sort + stack	Merge overlapping intervals sequentially
Word Search in 2D Grid	DFS / Backtracking	Explore neighbors recursively, mark visited
Serialize/Deserialize Binary Tree	Preorder traversal	Use delimiters, recursive serialize/deserialize
2️⃣ Databases & Transactions
Question	Key Points	Solution Hints
ACID vs BASE	ACID → strong consistency; BASE → eventual consistency	Use ACID for payments, BASE for caching/recommendations
Explain isolation levels	READ COMMITTED, REPEATABLE READ, SERIALIZABLE	Use examples: double booking seats, lost updates
How to scale DB for millions of writes	Sharding, replication, partitioning	Shard by user_id, read replicas, async writes for non-critical
Indexing strategy	Composite index, covering index, query optimization	Add index for search fields, avoid over-indexing
SQL vs NoSQL use cases	Transactions vs flexible schema	Orders → SQL, Chat → NoSQL, Recommendations → NoSQL
3️⃣ APIs & Backend
Question	Key Points	Solution Hints
Rate-limited REST API	Token bucket / leaky bucket	Track per user requests in Redis
Idempotent payment API	Retry safe	Use idempotency key, DB constraints
OAuth2 flow	Auth code, token, refresh token	Client → Auth server → Access token → Resource
Millions of concurrent WebSocket connections	Horizontal scaling	Use Redis pub/sub, sticky sessions, sharding connections
REST vs GraphQL	Fetch efficiency	GraphQL for selective fields, REST for simpler endpoints
4️⃣ CI/CD & DevOps
Question	Key Points	Solution Hints
Canary deployment vs Rolling update	Canary = small % first, monitor	Rolling = sequential servers, gradual traffic shift
Debugging failed CI/CD	Logs, build artifacts	Check unit tests, integration tests, docker builds
Kubernetes pod scaling	HPA, metrics	CPU/memory-based auto-scaling, multiple replicas
Monitoring microservices	Metrics, alerts	Track latency, failures, error rate, SLA breaches
Event-driven pipelines	Kafka/SQS	Async updates: notifications, recommendations, analytics
5️⃣ Cloud Platforms
Question	Key Points	Solution Hints
Multi-region global system	Geo-DNS, data replication	Deploy app servers + DB in multiple regions, CDN edge nodes
Serverless vs containerized	Scaling, cost	Serverless: auto-scale, pay-per-use; Containers: more control, persistent workload
Petabyte storage	Object storage, lifecycle	S3/GCS, Glacier/Coldline for old data
Cost optimization	Reserved instances, spot instances	Scale down unused servers, cache hot content, compress assets
6️⃣ Security & Authentication
Question	Key Points	Solution Hints
SSO with SAML	IdP, SP, assertions	Identity provider signs assertion, service provider validates
JWT vs OAuth2	Token-based, stateless	JWT stores claims, OAuth2 manages access tokens + refresh
Secure payment flow	TLS, idempotency, PCI compliance	Encrypt data at rest & transit, validate inputs
Rate-limiting abuse prevention	Throttle endpoints	Redis counters per user, sliding window or token bucket
DRM for streaming	Content encryption	Generate signed URLs, restrict playback devices
7️⃣ System Design (5 Systems)
Question	Key Points	Solution Hints
Chat app: millions of users	WebSockets, Redis pub/sub, DB sharding	Maintain presence in Redis, queue offline messages, sharding by user_id
E-Commerce: inventory consistency	Transactions, event-driven	Use SQL for orders, async updates for inventory & recommendations
Video streaming: adaptive bitrate	CDN, multi-resolution	HLS/DASH, edge caching, serverless transcoding
Job portal: search & recommendations	ElasticSearch, async computation	Precompute recommendations, cache hot queries, shard DB
Scaling strategy	Horizontal vs vertical	Stateless microservices, auto-scale pods/servers, multi-region deployment
8️⃣ Monitoring & Observability
Question	Key Points	Solution Hints
Detect slow API	Metrics: latency percentiles	Track P95/P99 latency, alerts when threshold breached
Real-time message delivery	Metrics, retries	Monitor WebSocket connection drops, delivery failures
Failed jobs / async pipeline	Logs + alerts	Use DLQ (dead-letter queue) for retries, alert if failure threshold crossed
✅ How to Use This Bank
Pick one domain per day: DSA, DB, API, Cloud, CI/CD, Security, System Design.

Read the question, recall key points, attempt solution hints.

After answering, compare with best practices and trade-offs.

Simulate real interview pressure: 20–30 min per problem, explain reasoning aloud.

Repeat across all domains and systems.
