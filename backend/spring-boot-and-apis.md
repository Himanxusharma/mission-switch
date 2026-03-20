# Spring Boot, REST APIs & Authentication Basics

> **Source:** Extracted from `notes/All_chats.md` (Akamai SDE-II prep). Content preserved; reorganized into Concepts vs Interview sections.

**How to read:** Start with **At a glance** / talk track if present, then the full chapter. **Fenced code blocks** are copy-paste examples; **tables** compare options; **ASCII diagrams** use monospace — widen the pane or scroll horizontally.

## Concepts

> *Skim **At a glance** first — a short on-ramp. Below the line is the full chapter.*

---

### At a glance · Spring / REST

- **Core story:** **IoC container** wires implementations to interfaces; **Boot** is opinionated auto-config + embedded server + starters.
- **REST:** resources, **idempotent** methods, **status codes**, validation, **global exception** handling.
- **Security:** **filter chain**, JWT in header, where **OAuth2** fits vs **resource server**.

#### Talk track (~60 s)

**`@SpringBootApplication`** triggers component scan and auto-config. **`@RestController`** + **`@RequestMapping`** expose HTTP. **`@Service` / `@Repository`** for layers; **`@Autowired`** constructor injection preferred. **`application.yml`** for config profiles. Exceptions → **`@ControllerAdvice`** for consistent error JSON. Security: **`SecurityFilterChain`** (Boot 3) customizes **authorizeHttpRequests**, **JWT** resource server or custom filter.

#### Easy mistakes

- **Singleton beans** + mutable state → thread safety.  
- **Transaction boundaries:** `@Transactional` on **self-invocation** (proxy) doesn’t work — know why.  
- **Giant controllers** — mention splitting by domain and **DTO validation**.

#### Quick checks

- [ ] Explain **DI** without saying “magic.”  
- [ ] **401 vs 403** in your own words.  
- [ ] One **validation + error body** example.

---
### Spring Boot, APIs & authentication

🧠 PART 1: What is Spring & Spring Boot?
🔹 What is Spring?
Spring is a Java framework that helps you:

Build backend applications

Manage objects automatically

Reduce boilerplate code

🔥 Problem Spring Solves
Without Spring:

You manually create objects

Manage dependencies yourself

Tight coupling ❌

💡 Spring Solution:
Inversion of Control (IoC)

👉 Meaning:

Spring creates and manages objects for you

⚙️ Dependency Injection (DI)
Instead of:

UserService service = new UserService();
Spring does:

@Autowired
UserService service;
👉 This is Dependency Injection

🚀 What is Spring Boot?
Spring Boot = Spring + Auto Configuration + Production Ready

🔥 Why it matters:
No XML configs

Embedded server (Tomcat)

Faster development

🧱 PART 2: Building a REST API (Core Skill)
🔹 What is REST API?
REST = way to communicate between systems using HTTP

🌐 HTTP Methods
Method	Purpose
GET	Fetch data
POST	Create
PUT	Update
DELETE	Remove
💻 Example: User API
1️⃣ Controller
@RestController
@RequestMapping("/users")
public class UserController {

    @GetMapping
    public List<String> getUsers() {
        return List.of("A", "B");
    }

    @PostMapping
    public String createUser() {
        return "User created";
    }
}
2️⃣ Service Layer
@Service
public class UserService {
    public String getData() {
        return "data";
    }
}
3️⃣ Repository Layer
@Repository
public interface UserRepository {
}
🧠 Architecture Flow
Client → Controller → Service → Repository → DB
🔥 PART 3: Exception Handling
❌ Bad Practice:
Returning raw errors

✅ Good Practice:
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(Exception.class)
    public String handleException(Exception ex) {
        return ex.getMessage();
    }
}
👉 Interview Tip:

“I prefer centralized exception handling for consistency”

🔐 PART 4: Authentication & Security (CRITICAL FOR JD)
This is where most candidates fail.

🔹 What is Authentication?
“Who are you?”

🔹 What is Authorization?
“What can you access?”

🔥 OAuth 2.0 (Core)
💡 Real Example:
Login with Google

🧠 Flow:
User clicks login

Redirect to provider

User approves

Token is returned

🔑 Key Components:
Client

Authorization Server

Resource Server

Access Token

🔥 JWT (JSON Web Token)
💡 What is JWT?
A token used for authentication

⚙️ Structure:
Header.Payload.Signature
💻 Example Flow:
User logs in

Server returns JWT

Client sends JWT in every request

🔥 SAML (Mentioned in JD)
💡 Used in:
Enterprise SSO systems

🧠 Difference from OAuth:
Feature	OAuth	SAML
Format	JSON	XML
Use case	Apps	Enterprise login
👉 You don’t need deep code—just concept clarity

🧱 PART 5: API Design Best Practices (INTERVIEW GOLD)
🔥 Must Follow:
✔ Use proper status codes
200 → OK

201 → Created

400 → Bad request

500 → Server error

✔ Naming conventions
GET /users
POST /users
GET /users/{id}
✔ Versioning
/api/v1/users
✔ Pagination
GET /users?page=1&size=10
⚙️ PART 6: Real-World Concepts (Akamai Level)
🔥 Scalability Thinking
👉 Example:

“If API gets 1M requests/min?”

You should say:

Load balancer

Caching (Redis)

Horizontal scaling

🔍 Logging & Monitoring
Tools mentioned in JD:

Splunk

New Relic

👉 Say:

“I use centralized logging for debugging production issues”

🧪 PART 7: Practice Tasks (MANDATORY)
✅ Task 1:
Build API:

GET /users

POST /users

✅ Task 2:
Explain:

OAuth vs JWT vs SAML

✅ Task 3:
Answer:

“How do you secure an API?”

✅ Task 4:
Add:

Exception handling

Proper status codes

🎯 INTERVIEW QUESTIONS (YOU WILL GET)
🔥 MUST PREPARE:
What is Dependency Injection?

How does Spring Boot auto-config work?

How do you secure APIs?

Difference between PUT vs PATCH

Stateless vs Stateful APIs

🚀 PRO STRATEGY
When answering:

👉 Always say:

“In production systems…”

Example:

“In production, I use JWT with expiration and refresh tokens…”


Take Spring Boot + API + Auth mock interview

Ask real Akamai-level questions


## Interview questions, mocks & scenarios

yes Take Spring Boot + API + Auth mock interview

Ask real Akamai-level questions


🎯 MOCK INTERVIEW — Spring Boot + API + Auth
⚠️ Same rules:

Answer one question at a time

Be structured

I will interrupt/correct like a real interviewer

🧠 Question 1: Dependency Injection (Foundation → Depth)
👉 Explain Dependency Injection in Spring Boot

❗ But this is NOT enough:
If you just say definition → ❌ reject

✅ Your answer MUST include:
What problem it solves

How Spring implements it

Types of DI

Real-world example

Why it improves scalability

👉 Bonus (this is SDE-2 level):

Difference between @Autowired vs constructor injection

What is IoC container?

⚙️ Question 2: API Design (REAL-WORLD)
👉 Design an API for:

User Service (Production Ready)

Requirements:
Create user

Get user by ID

Update user

Delete user

❗ Your answer MUST include:
Endpoints (proper REST naming)

HTTP methods

Status codes

Request/response structure

Error handling strategy

👉 Bonus:

Pagination

Versioning

🔐 Question 3: Authentication (CRITICAL)
👉 How would you secure a REST API?

❗ Don’t give generic answer
✅ You MUST include:
JWT flow (step by step)

Where token is stored

How validation works

Expiry & refresh tokens

👉 Bonus:

Difference between JWT and OAuth

When to use each

⚡ Question 4: Debugging Scenario (REAL AKAMAI STYLE)
👉 Situation:

Your API suddenly becomes slow under high traffic (1M requests/min)

❗ What will you do?
✅ You MUST cover:
Identification (logs, monitoring)

Bottleneck analysis

Fixes (DB, caching, scaling)

👉 Bonus:

Mention tools like:

Splunk

New Relic

🧱 Question 5: Spring Boot Internals (SDE-2 LEVEL)
👉 How does Spring Boot auto-configuration work?

✅ Expected:
@SpringBootApplication

@EnableAutoConfiguration

Classpath scanning

Conditional beans

⚔️ Final Boss Question (THIS DECIDES LEVEL)
👉 Stateless vs Stateful APIs

❗ Explain with:
Real-world example

Why modern systems prefer stateless

Impact on scalability


Interrupt you

Fix gaps

Push deeper until it’s Akamai-ready
