# Object-Oriented Programming (OOP)

> **Source:** Extracted from `notes/All_chats.md` (Akamai SDE-II prep). Content preserved; reorganized into Concepts vs Interview sections.

**How to read:** Start with **At a glance** / talk track if present, then the full chapter. **Fenced code blocks** are copy-paste examples; **tables** compare options; **ASCII diagrams** use monospace — widen the pane or scroll horizontally.

## Concepts

> *Skim **At a glance** first — a short on-ramp. Below the line is the full chapter.*

---

### At a glance · OOP

- **Interviewers want:** design sense, not textbook definitions — use **payment / checkout / notification** style examples.
- **Structure answers:** identify **nouns → classes**, **verbs → methods**, mark **what varies** (strategy) vs **stable contracts** (interfaces).
- **Always mention:** **composition over inheritance** when behavior stacks unpredictably.

#### Talk track (~90 s)

**`Payment`** abstraction; **`CreditCardPayment`**, **`WalletPayment`** polymorphic `pay()`. **`Order`** aggregates line items; **`PricingEngine`** (composition) applies rules. Hide secrets behind **`PaymentGatewayClient`** interface. **Encapsulation** on balances and state; **interface** for test doubles.

#### Easy mistakes

- Deep **inheritance trees** for variants → prefer **composition + strategy**.  
- **God objects** that know DB + email + rules — split responsibilities.  
- Confusing **interface** vs **abstract class** — give a **rule of thumb** (multiple capability contracts vs shared partial implementation).

#### Quick checks

- [ ] Four pillars with **one non-toy** example each.  
- [ ] **Interface vs abstract class** in one sentence each.  
- [ ] Name two **design patterns** you’ve actually shipped.

🧠 1. OOP Concepts (Interview Critical)
You MUST be crystal clear on:

🔹 4 Pillars
Encapsulation

Inheritance

Polymorphism

Abstraction

💥 How Interviewers Ask
Instead of definitions, they ask:

👉 “Design a payment system using OOP”

💡 Your Answer Structure:
abstract class Payment {
    abstract void pay(double amount);
}

class CreditCardPayment extends Payment {
    void pay(double amount) {
        System.out.println("Paid via Credit Card");
    }
}

class UpiPayment extends Payment {
    void pay(double amount) {
        System.out.println("Paid via UPI");
    }
}
🎯 What they’re checking:
Abstraction ✔

Polymorphism ✔

Extensibility ✔

⚠️ Must-Know Follow-ups:
Interface vs Abstract Class

Method Overloading vs Overriding

Composition vs Inheritance
🧩 PART 3: OOP (CORE OF EVERYTHING)
Let’s build intuition first 👇

🔹 Why OOP?
Real world is made of objects:

Car 🚗

User 👤

Payment 💳

OOP helps us model this in code.

🧠 4 Pillars of OOP (DEEP UNDERSTANDING)
1️⃣ Encapsulation (Data Protection)
💡 Idea:
“Hide internal data, expose only necessary parts”

💻 Example:
class BankAccount {
    private double balance;

    public void deposit(double amount) {
        balance += amount;
    }

    public double getBalance() {
        return balance;
    }
}
🔥 Why important?
Prevents misuse

Secure code

2️⃣ Inheritance (Code Reuse)
💡 Idea:
“Child class can use parent class properties”

💻 Example:
class Animal {
    void eat() {
        System.out.println("Eating...");
    }
}

class Dog extends Animal {
    void bark() {
        System.out.println("Barking...");
    }
}
3️⃣ Polymorphism (Same action, different behavior)
🔥 Two types:
➤ Compile-time (Overloading)
int add(int a, int b) { return a + b; }
int add(int a, int b, int c) { return a + b + c; }
➤ Runtime (Overriding)
class Animal {
    void sound() { System.out.println("Animal sound"); }
}

class Dog extends Animal {
    void sound() { System.out.println("Bark"); }
}
4️⃣ Abstraction (Hide complexity)
💡 Idea:
“Show WHAT, hide HOW”

💻 Example:
abstract class Payment {
    abstract void pay();
}
⚔️ IMPORTANT: Interface vs Abstract Class
Feature	Interface	Abstract Class
Methods	Only abstract (mostly)	Abstract + concrete
Use	Multiple inheritance	Base class
Example	Payment gateway	Vehicle

## Interview questions, mocks & scenarios


🎯 ROUND 1: Java + OOP + HashMap (Day 1 Test)
🧠 Question 1: OOP (Warm-up but tricky)
👉 Design a Payment System

Requirements:

Support multiple payment types (Card, UPI, NetBanking)

Easy to add new payment methods in future

Follow OOP principles

❓ Your Task:
Write Java code

Explain which OOP principles you used

Explain why your design is scalable

⚙️ Question 2: Core Java
👉 Explain how HashMap works internally

❓ Your Answer MUST include:
Hashing

Index calculation

Collision handling

Load factor

Rehashing

👉 Bonus:

What changed after Java 8?

💥 Question 3: Coding (Medium)
👉 Two Sum Problem

Problem:
Given an array and a target, return indices of 2 numbers that add up to target.

❓ Example:
nums = [2,7,11,15], target = 9
Output: [0,1]
Requirements:
First give brute force

Then optimized solution

Time & space complexity

🧵 Question 4: Multithreading (Conceptual)
👉 What is:

Race condition?

Synchronization?

Deadlock?

👉 Give real-world analogy

⚠️ Rules (Important)
Answer like you're in interview (structured)

Don’t rush

If stuck → say “hint”
