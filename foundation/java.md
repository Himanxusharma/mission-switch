# Java Core: JVM, Memory, Collections, HashMap & Concurrency

> **Source:** Extracted from `notes/All_chats.md` (Akamai SDE-II prep). Content preserved; reorganized into Concepts vs Interview sections.

**How to read:** Start with **At a glance** / talk track if present, then the full chapter. **Fenced code blocks** are copy-paste examples; **tables** compare options; **ASCII diagrams** use monospace — widen the pane or scroll horizontally.

## Concepts

> *Skim **At a glance** first — a short on-ramp. Below the line is the full chapter.*

---

### At a glance · Java core

- **They test:** can you go **past syntax** — memory model, collections internals, **concurrency**, and tying answers to **production** (e.g. `ConcurrentHashMap`).
- **Order:** definition → **how it works** → limitation → **when you’d use something else**.
- **Don’t:** memorize API only; **do:** explain **trade-offs** (e.g. lock contention, false sharing at high level).

#### Talk track (~60 s)

JVM runs **bytecode**; **stack** for frames/locals, **heap** for objects. **GC** reclaims unreachable heap objects. **HashMap**: buckets, hash, equals, resize; not thread-safe → **`ConcurrentHashMap`** for concurrent maps. **Strings** immutable for security/caching. Concurrency: **`synchronized`**, **`volatile`** visibility, **deadlock** when circular waits.

#### Easy mistakes

- **`==` vs `equals`** on `Integer` / `String` / custom types.  
- **“HashMap is O(1)”** — amortized; worst case chains/treeify.  
- **“Just add synchronized everywhere”** → throughput collapse; mention **granularity** and **java.util.concurrent** tools.

#### Quick checks

- [ ] Explain **HashMap** and **ConcurrentHashMap** out loud.  
- [ ] **StackOverflowError** vs **OutOfMemoryError** (heap).  
- [ ] One **deadlock** example and how you’d prevent/detect.

---
### Java Core + OOP + Collections (Deep + Practical)


⚙️ 2. Java Internals (HIGH IMPACT)
🔹 Heap vs Stack
Stack → method calls

Heap → objects

👉 Question:

“Why do we get StackOverflowError?”

🔹 String Internals
👉 Most asked:

Why is String immutable?

String vs StringBuilder vs StringBuffer

🔹 == vs equals()
👉 Clean explanation:

== → reference

.equals() → value

🧱 3. Collections Framework (Important)
This is where many candidates fail.

🔥 A. HashMap (MOST ASKED)
👉 Core Question:
“How does HashMap work internally?”

💡 Your Answer (Structured)
Uses array of buckets

Hash function → index

Collision handling:

Linked List

Red-Black Tree (Java 8+)

⚡ Important Concepts:
Load Factor (0.75)

Rehashing

Hash collisions

💻 Code Example:
Map<String, Integer> map = new HashMap<>();
map.put("A", 1);
map.put("B", 2);
🔥 B. HashMap vs ConcurrentHashMap
👉 Interview Gold Question

Feature	HashMap	ConcurrentHashMap
Thread Safe	❌	✅
Locking	None	Segment / bucket level
Performance	Faster (single thread)	Better in multi-thread
🔥 C. List vs Set vs Map
List → ordered, duplicates allowed

Set → no duplicates

Map → key-value

🧵 4. Multithreading Basics
Even basic knowledge gives HUGE advantage.

🔹 Key Concepts:
Thread vs Process

synchronized

Deadlock

💥 Interview Question:
“What is synchronization?”

👉 Answer:

Controls access to shared resources

Prevents race conditions

🧪 5. Practice Questions (DO THESE TODAY)
🟢 Easy
Reverse a string

Find duplicates in array

🟡 Medium
LRU Cache

Two Sum

Valid Parentheses

### Practice (verbal + code)

1. Explain out loud how **HashMap** works internally.
2. Write one **polymorphism** example and one **abstraction** example from a real domain.
3. Solve **Two Sum** and a basic **LRU** (conceptual or coded).

**Framing:** connect answers to production (e.g. `HashMap` is not thread-safe; concurrent maps use **`ConcurrentHashMap`**).

**Deeper checklist**

1. Explain **stack vs heap** and **HashMap** mechanics in your own words.
2. Code a small class that exercises all **four OOP pillars**.
3. **Two Sum** and **reverse string** under time pressure.

### Deep dive: JVM, memory, collections

🧠 PART 1: What is Java? (Foundation)
Java is:

A programming language

Used to build backend systems, APIs, large-scale applications

🔥 Key Property:
“Write Once, Run Anywhere”

👉 Because of JVM (Java Virtual Machine)

⚙️ How Java Actually Runs
You write code → .java

Compiler converts → .class (bytecode)

JVM runs it

👉 Flow:

.java → compiler → bytecode → JVM → machine execution
🧱 PART 2: Memory Model
Understanding this = instant advantage

🔹 Stack vs Heap
🧠 Stack (Fast, small)
Stores:

Method calls

Local variables

🧠 Heap (Large, slower)
Stores:

Objects (created using new)

💻 Example:
class Test {
    public static void main(String[] args) {
        int x = 10;              // Stack
        Person p = new Person();// Reference in stack, object in heap
    }
}
🔥 Interview Question:
Why do we get StackOverflowError?

👉 Answer:

Infinite recursion fills stack memory

🧱 PART 4: Collections Framework (CRITICAL)
This is where interviews get serious.

🔹 Why Collections?
Instead of arrays → flexible data structures:

Dynamic size

Better operations

🧠 Types of Collections
🔸 1. List (Ordered, duplicates allowed)
List<Integer> list = new ArrayList<>();
list.add(1);
list.add(1); // allowed
🔸 2. Set (No duplicates)
Set<Integer> set = new HashSet<>();
set.add(1);
set.add(1); // ignored
🔸 3. Map (Key-value)
Map<String, Integer> map = new HashMap<>();
map.put("A", 1);
🔥 PART 5: HashMap (DEEP DIVE — MUST MASTER)
💡 What is HashMap?
Stores:

Key → Value
⚙️ How it works internally (STEP BY STEP)
1️⃣ Hashing
Every key generates a hash code

int hash = key.hashCode();
2️⃣ Index Calculation
index = hash % array_size;
3️⃣ Storage
Data stored in bucket (array index)

4️⃣ Collision Handling
If 2 keys go to same index:

👉 Java uses:

Linked List (before Java 8)

Red-Black Tree (after threshold)

💻 Visual:
Index 0 → (A,1) → (B,2)
Index 1 → (C,3)
🔥 Important Concepts
✔ Load Factor
Default: 0.75

When exceeded → resize

✔ Rehashing
New bigger array


⚠️ Interview Questions
👉 Why HashMap is not thread-safe?

👉 How to make it thread-safe?

Use ConcurrentHashMap

🧵 PART 6: Multithreading Basics
🔹 What is Thread?
Smallest unit of execution

🔥 Problem: Race Condition
2 threads modify same data → wrong result

🔒 Solution: Synchronization
synchronized void increment() {
    count++;
}
⚠️ Deadlock (Important)
When:

Thread A waits for B

Thread B waits for A

🎯 PART 7: INTERVIEW MINDSET
When asked ANY question:

👉 Always answer like:

Definition

Internal working

Real-world use

Limitation

Optimization

## Interview questions & practice

_Use the concepts above; drill out loud with a timer._

**Quick checks**

- Why is **HashMap** not thread-safe? How do you make concurrent access safe (**ConcurrentHashMap**)?
- **Stack vs heap**, `StackOverflowError`, **String** immutability, **==** vs **equals**
- **Multithreading**: race conditions, **synchronized**, deadlock (plus a real-world analogy)

**Coding drills** (from the concepts section)

- Two Sum, LRU (basic), Valid Parentheses, reverse string, find duplicates
