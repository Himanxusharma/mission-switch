# CI/CD, Docker, Kubernetes & DevOps Scenario Q&A

> **Source:** Extracted from `notes/All_chats.md` (Akamai SDE-II prep). Content preserved; reorganized into Concepts vs Interview sections.

**How to read:** Start with **At a glance** / talk track if present, then the full chapter. **Fenced code blocks** are copy-paste examples; **tables** compare options; **ASCII diagrams** use monospace — widen the pane or scroll horizontally.

## Concepts

> *Skim **At a glance** first — a short on-ramp. Below the line is the full chapter.*

---

### At a glance · CI/CD, Docker, K8s

- **CI:** fast feedback — **lint, unit tests, build image** on every PR.  
- **CD:** promote **immutable artifacts**; **environment-specific config**, not baked secrets.  
- **K8s:** **Pod** (smallest runnable), **Deployment** (desired replicas), **Service** (stable IP/DNS), **Ingress** (HTTP routing).

#### Talk track (~60 s)

Pipeline: **commit** → **build** Docker image → **scan** → push to registry → **deploy** to cluster (**rolling** or **canary**). K8s **schedules** pods on nodes; **liveness/readiness** gates traffic; **HPA** scales on CPU/custom metrics. **ConfigMaps/Secrets** inject env; **zero-downtime** via **maxUnavailable/maxSurge**. Rollback = **previous ReplicaSet** or **helm rollback**.

#### Easy mistakes

- **Mutable** servers; **snowflake** config.  
- **Latest** tag in prod — pin **digests** or semver tags.  
- **Resource limits** unset → noisy neighbor OOM.

#### Quick checks

- [ ] **Blue-green vs canary** one-liner each.  
- [ ] What **readiness** should check (DB up, warmup).  
- [ ] Where **secrets** live (not in Git).

🚀 CI/CD DEEP DIVE (SDE-2 LEVEL)
🧠 PART 1: WHAT IS CI/CD (REAL UNDERSTANDING)
💡 CI = Continuous Integration
👉 Developers frequently:

Push code

Run tests automatically

💡 CD = Continuous Delivery / Deployment
👉 Code is:

Built

Tested

Deployed

🔥 Pipeline Flow
Code → Build → Test → Package → Deploy → Monitor
🧠 Interview Line:
“CI/CD automates the software delivery lifecycle, ensuring faster and reliable deployments”

⚙️ PART 2: PIPELINE STAGES (INTERNAL)
1️⃣ Code Commit
Push to Git (e.g., Git)

2️⃣ Build
Compile code

Resolve dependencies

3️⃣ Test
Unit tests

Integration tests

4️⃣ Package
Create artifact (JAR, Docker image)

5️⃣ Deploy
Push to server/cloud

6️⃣ Monitor
Logs, metrics

🧱 PART 3: TOOLS ECOSYSTEM
🔥 CI/CD Tools
Jenkins

GitHub Actions

GitLab CI/CD

🔥 Containerization
Docker

🔥 Orchestration
Kubernetes

🧠 PART 4: INTERNAL WORKING
💡 Example Flow
Step 1: Developer Pushes Code
git push origin main
Step 2: CI Trigger
👉 Pipeline starts automatically

Step 3: Build + Test
mvn clean install
npm test
Step 4: Docker Image
docker build -t app:v1 .
Step 5: Deploy
Push to Kubernetes

🧠 PART 5: DEPLOYMENT STRATEGIES
🔥 1. Blue-Green Deployment
👉 Two environments:

Blue (live)

Green (new)

Switch traffic instantly

🔥 2. Canary Deployment
👉 Release to small % users

🔥 3. Rolling Deployment
👉 Gradual update

🧠 PART 6: PIPELINE OPTIMIZATION
⚡ Speed
Parallel jobs

Cache dependencies

⚡ Reliability
Fail fast

Retry mechanisms

⚡ Security
Secrets management

Vulnerability scans

🧠 PART 7: REAL INTERVIEW SCENARIOS
💣 SCENARIO 1
👉 “Build CI/CD pipeline for Spring Boot app”

✅ Answer
“I would configure a pipeline that triggers on Git push, runs unit tests, builds the JAR, creates a Docker image, and deploys it to Kubernetes using rolling deployment.”

💣 SCENARIO 2
👉 “How to avoid broken production deploy?”

✅ Answer
“Use automated tests, staging environment, and deployment strategies like canary or blue-green to reduce risk.”

💣 SCENARIO 3
👉 “Pipeline is slow—what will you do?”

✅ Answer
“I would optimize by caching dependencies, running jobs in parallel, and reducing unnecessary steps.”

💣 SCENARIO 4
👉 “How to handle secrets?”

✅ Answer
“Use secure vaults or environment variables, never hardcode secrets in code or pipeline configs.”

💣 SCENARIO 5 (ADVANCED)
👉 “How to rollback failed deployment?”

✅ Answer
“Use versioned deployments and rollback to previous stable version via Kubernetes or deployment tool.”

🧠 PART 8: END-TO-END REAL SYSTEM
💥 Example Architecture
Developer → Git → CI Pipeline → Docker → Kubernetes → Production
🧠 PART 9: COMMON MISTAKES
❌ No tests in pipeline
❌ Deploy directly to production
❌ No rollback strategy
❌ Hardcoded secrets

🎯 FINAL MENTAL MODEL
Think like:

CI/CD = Automation + Reliability + Speed
### Practice
Answer:

1️⃣ How would you design CI/CD for Node + Spring app?
2️⃣ Difference between CI and CD?
3️⃣ How to make pipeline faster?

👉 “Full backend mock interview (final)”
👉 “Last-day revision cheat sheet”


Grill me DevOps + CI/CD scenarios (hard)

Now this is real DevOps + CI/CD grilling—exactly what separates developers from production engineers.

⚠️ Same rules:

Structured answers

Mention tools + internals + trade-offs

No generic lines

💣 SCENARIO 1: BROKEN PRODUCTION DEPLOY
👉 “You deployed a new version and production is DOWN”

❗ What will you do?
🎯 Expectation:
Immediate mitigation

Rollback strategy

Root cause

💣 SCENARIO 2: ZERO-DOWNTIME DEPLOYMENT
👉 “How do you deploy without downtime?”

🎯 Must include:
Deployment strategy

Traffic switching

💣 SCENARIO 3: SLOW CI PIPELINE
👉 “Pipeline takes 20 minutes”

🎯 Must include:
Bottleneck detection

Optimization

💣 SCENARIO 4: MULTI-ENVIRONMENT SETUP
👉 “Dev, staging, prod environments”

🎯 Expectation:
Config management

Secrets handling

💣 SCENARIO 5: MICROSERVICES CI/CD
👉 “10+ services need deployment”

🎯 Must include:
Independent pipelines

Versioning

Orchestration

💣 SCENARIO 6: SECURITY BREACH IN PIPELINE
👉 “Secrets leaked in logs”

🎯 Expectation:
Immediate action

Prevention

💣 SCENARIO 7: ROLLBACK STRATEGY
👉 “Deployment partially failed”

🎯 Must include:
Versioning

Safe rollback

💣 SCENARIO 8: HIGH TRAFFIC RELEASE
👉 “New feature rollout to millions”

🎯 Expectation:
Canary deployment

Monitoring

💣 SCENARIO 9: INFRA FAILURE
👉 “Server crashes during deploy”

🎯 Must include:
Resilience

Auto-recovery

💣 SCENARIO 10: LOGGING & MONITORING
👉 “How do you detect issues in production?”

🎯 Must include:
Logs

Metrics

Alerts


Challenge you

Add missing points

Upgrade to SDE-2 / Akamai-level

Let’s see how you handle real production pressure 😈🔥


answer all above


💣 SCENARIO 1: Production Down After Deploy
✅ Answer
“First, I would prioritize restoring service quickly:

Trigger rollback to last stable version (via deployment tool or Kubernetes rollout undo)

Check health metrics and logs (via Splunk / New Relic)

Once stable, perform root cause analysis:

Recent changes

Failed services

DB issues

Trade-off:

Prioritize availability first, then debugging.”

💣 SCENARIO 2: Zero-Downtime Deployment
✅ Answer
“I would use deployment strategies like:

Blue-Green deployment → switch traffic instantly

Rolling deployment → gradual replacement

Using Kubernetes:

New pods are created before old ones are terminated

This ensures no downtime during deployment.”

💣 SCENARIO 3: Slow CI Pipeline
✅ Answer
“I would:

Identify bottlenecks (build, test, deploy stages)

Optimize:

Cache dependencies

Parallelize jobs

Skip unnecessary steps

Tools like GitHub Actions support parallel execution

Trade-off:

Faster pipelines vs cost of compute resources.”

💣 SCENARIO 4: Multi-Environment Setup
✅ Answer
“I would maintain separate environments:

Dev → development

Staging → testing

Prod → live

Use:

Environment-specific configs

Secure secrets management (env variables or vaults)

This ensures safe testing before production deployment.”

💣 SCENARIO 5: Microservices CI/CD
✅ Answer
“For microservices:

Each service has its own pipeline

Independent deployment

Versioning per service

Use containerization via Docker and orchestration via Kubernetes

This allows scalability and isolation of failures.”

💣 SCENARIO 6: Security Breach (Secrets Leak)
✅ Answer
“Immediate actions:

Revoke exposed secrets

Rotate credentials

Audit logs

Prevention:

Never log secrets

Use secret managers

Trade-off:

Security over convenience.”

💣 SCENARIO 7: Rollback Strategy
✅ Answer
“I would:

Maintain versioned deployments

Use rolling back to previous stable version

In Kubernetes:

kubectl rollout undo

This ensures quick recovery from failures.”

💣 SCENARIO 8: High Traffic Release
✅ Answer
“I would use:

Canary deployment (release to small % users)

Monitor metrics

Tools:

New Relic for performance

Trade-off:

Slower rollout but safer deployment.”

💣 SCENARIO 9: Infra Failure During Deploy
✅ Answer
“I would design for resilience:

Use multiple instances

Auto-scaling

Health checks

With Kubernetes:

Failed pods are restarted automatically

This ensures high availability.”

💣 SCENARIO 10: Logging & Monitoring
✅ Answer
“I would implement:

Centralized logging → Splunk

Metrics monitoring → New Relic

Alerts for anomalies

This enables proactive issue detection.”

🧠 WHAT YOU JUST MASTERED
You can now:

Handle production failures

Design CI/CD pipelines

Think in reliability + scalability

🎯 FINAL INTERVIEW EDGE
👉 Always answer like:

Problem → Immediate action → Long-term fix → Trade-off

Now you’re READY for:

👉 “Last-day revision cheat sheet (super important)”

You’re operating at real SDE-2 production engineer level 💯🔥

docker and kubernates

Now we’re at Docker + Kubernetes (core DevOps + backend infra)—this is must-know for SDE-2 and very relevant for companies like Akamai Technologies.

We’ll go:
👉 Concept → Internals → Commands → Real scenarios → Interview answers

🐳 PART 1: WHAT IS DOCKER (REAL UNDERSTANDING)
💡 Definition
👉 Docker = containerization platform

🧠 Idea
App + Dependencies → Container → Runs anywhere
🔥 Why Docker?
No “works on my machine” issue

Lightweight (vs VM)

Fast startup

⚙️ PART 2: DOCKER INTERNALS
🧱 Components
1️⃣ Image
👉 Blueprint of app

2️⃣ Container
👉 Running instance of image

3️⃣ Docker Engine
👉 Runtime that runs containers

🧠 Layers
Base Image → Dependencies → App Code
👉 Each layer cached → faster builds

🧑‍💻 PART 3: DOCKER HANDS-ON
🔥 Dockerfile Example
FROM node:18

WORKDIR /app
COPY package.json .
RUN npm install

COPY . .
CMD ["node", "server.js"]
🔥 Commands
docker build -t app:v1 .
docker run -p 3000:3000 app:v1
docker ps
docker stop <id>
🧠 PART 4: DOCKER NETWORKING
Types:
Bridge (default)

Host

Overlay (for distributed systems)

🧠 PART 5: DOCKER PROBLEMS
❌ Not good for orchestration
❌ Hard to manage at scale

👉 That’s where Kubernetes comes 👇

☸️ PART 6: WHAT IS KUBERNETES
💡 Definition
👉 Kubernetes = system to manage containers at scale

🧠 What it does
Deploy → Scale → Heal → Manage containers
⚙️ PART 7: KUBERNETES INTERNALS
🧱 Core Components
1️⃣ Pod
👉 Smallest unit (1+ containers)

2️⃣ Node
👉 Machine running pods

3️⃣ Cluster
👉 Group of nodes

4️⃣ Deployment
👉 Manages replicas

5️⃣ Service
👉 Exposes app

🧠 FLOW
User → Service → Pod → Container
🧑‍💻 PART 8: KUBERNETES YAML
🔥 Deployment Example
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
        - name: app
          image: app:v1
          ports:
            - containerPort: 3000
🧠 PART 9: AUTO-SCALING
👉 Kubernetes can:

Scale pods automatically

Restart failed containers

🧠 PART 10: REAL INTERVIEW SCENARIOS
💣 SCENARIO 1
👉 “Why Docker?”

✅ Answer
“Docker ensures consistent environments by packaging application and dependencies into containers.”

💣 SCENARIO 2
👉 “Why Kubernetes?”

✅ Answer
“Kubernetes manages containerized applications at scale, providing auto-scaling, self-healing, and load balancing.”

💣 SCENARIO 3
👉 “App crashes—what happens?”

✅ Answer
“Kubernetes automatically restarts failed containers using health checks.”

💣 SCENARIO 4
👉 “How to scale app?”

✅ Answer
kubectl scale deployment app --replicas=5
💣 SCENARIO 5
👉 “Zero downtime deployment?”

✅ Answer
“Kubernetes rolling updates replace pods gradually without downtime.”

🧠 PART 11: DOCKER vs KUBERNETES
Feature	Docker	Kubernetes
Purpose	Containerize	Orchestrate
Scope	Single machine	Cluster
Scaling	Manual	Automatic
🎯 FINAL MENTAL MODEL
Docker → Package app  
Kubernetes → Run app at scale  
### Practice
Answer:

1️⃣ Why containers better than VMs?
2️⃣ What happens when pod crashes?
3️⃣ How Kubernetes does load balancing?

👉 “Final full mock interview (Akamai-level)” 😈🔥
👉 “1-page revision cheat sheet”


answer the above questions and also deep dive more into the concepts and real world and interview problems

We’ll do this in two parts:

Answer your 3 questions (interview-ready)

Deep dive into Docker + Kubernetes internals, real-world systems, and tricky interview problems

🧠 PART 1: DIRECT ANSWERS (SDE-2 LEVEL)
✅ 1️⃣ Why containers are better than VMs?
💡 Answer
“Containers are more lightweight than VMs because they share the host OS kernel, whereas VMs run a full OS for each instance.”

🔍 Deep Reason
Feature	Containers	VMs
OS	Shared	Separate
Startup	Seconds	Minutes
Resource usage	Low	High
🎯 Final Line
“Containers provide faster startup, better resource efficiency, and consistent environments compared to VMs.”

✅ 2️⃣ What happens when a Pod crashes?
💡 Answer
“In Kubernetes, if a pod crashes, the system automatically recreates it to maintain the desired state.”

🔍 Internals
Kubernetes uses desired state

Controller detects mismatch

New pod created

🎯 Final Line
“Kubernetes ensures self-healing by automatically restarting or recreating failed pods based on the desired state.”

✅ 3️⃣ How Kubernetes does load balancing?
💡 Answer
“Kubernetes uses Services to distribute traffic across multiple pods.”

🔍 Internals
Service has a virtual IP

Uses kube-proxy

Routes requests to pods

User → Service → Pod1 / Pod2 / Pod3
🎯 Final Line
“Kubernetes Services abstract pods and distribute traffic evenly, enabling built-in load balancing.”

🚀 PART 2: DEEP DIVE (THIS IS WHERE YOU LEVEL UP)
🐳 DOCKER INTERNALS (REAL ENGINEERING)
🔥 1. HOW DO CONTAINERS WORK?
👉 Not magic. Uses:

🧠 Linux features:
Namespaces → isolation

cgroups → resource limits

🔍 Example:
Process sees its own filesystem

But shares kernel

🔥 2. IMAGE LAYERS
Base OS → Node → App → Config
👉 Benefits:

Caching

Smaller builds

🔥 3. DOCKER REGISTRY
👉 Store images (Docker Hub, ECR)

☸️ KUBERNETES INTERNALS
🔥 1. CONTROL PLANE
Component	Role
API Server	Entry point
Scheduler	Assigns pods
Controller	Maintains state
etcd	Stores state
🔥 2. NODE COMPONENTS
kubelet → manages pods

kube-proxy → networking

🔥 3. DESIRED STATE MODEL
You say: “3 pods”
K8s ensures: always 3 pods
🧠 REAL WORLD ARCHITECTURE
💥 Example: Backend App
User → Load Balancer → Kubernetes → Pods → DB
🔥 FLOW
Request hits Load Balancer

Goes to Service

Service routes to Pod

Pod processes request

💣 REAL INTERVIEW PROBLEMS
🧠 SCENARIO 1
👉 “One pod is slow—what happens?”

✅ Answer
“Traffic is distributed across pods, so slow pod impacts only partial traffic. Health checks can remove unhealthy pods.”

🧠 SCENARIO 2
👉 “All pods crash”

✅ Answer
“Kubernetes recreates pods, but root cause must be fixed (bad image, config issue, resource limit).”

🧠 SCENARIO 3
👉 “How to deploy new version?”

✅ Answer
“Use rolling deployment to gradually replace old pods without downtime.”

🧠 SCENARIO 4
👉 “How to handle high traffic?”

✅ Answer
“Use horizontal pod autoscaling based on CPU/memory metrics.”

🧠 SCENARIO 5 (ADVANCED)
👉 “Pod cannot connect to DB”

✅ Debug Steps
Check env variables

Check network policies

Check service DNS

Check logs

🧠 ADVANCED CONCEPTS (SDE-2 EDGE)
🔥 1. LIVENESS vs READINESS PROBES
Liveness → restart container

Readiness → remove from traffic

🔥 2. CONFIGMAP & SECRETS
ConfigMap → non-sensitive data

Secrets → passwords

🔥 3. INGRESS
👉 External access to cluster

🎯 FINAL MENTAL MODEL
Think like:

Docker → Build once, run anywhere  
Kubernetes → Manage everything at scale  
🚀 FINAL INTERVIEW EDGE
Always answer:

Concept → Internals → Real use → Trade-off

You are READY for:

👉 “1-page revision cheat sheet before interview”


## Interview questions, mocks & scenarios

_(Embedded in Concepts above, or use sibling notes.)_
