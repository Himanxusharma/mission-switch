# Apache Kafka: Architecture, Diagram & Interview Q&A

> **Source:** Extracted from `notes/All_chats.md` (Akamai SDE-II prep). Content preserved; reorganized into Concepts vs Interview sections.

## Concepts

> *Skim **At a glance** first — a short on-ramp. Below the line is the full chapter.*

---

### At a glance · Kafka

- **Core:** **log-structured** broker; **topics/partitions**; **ordering per key**; **consumer groups** divide partitions.
- **Delivery:** **at-least-once** default; **duplicates** → **idempotent** consumers; **exactly-once** is nuanced (**transactions** / streams).
- **Ops:** **replication**, **ISR**, **leader election**, **consumer lag**, **rebalancing**.

#### Talk track (~60 s)

Producers write to **partitioned topics**; **key** chooses partition → **order** per key. **Brokers** persist **segments** on disk; **replication** for HA. **Consumer group** members share partitions **exclusively**. **Offsets** track progress; **commit** after processing for **at-least-once**. Failures: **retry** + **DLQ topic**; **reprocess** with **idempotent** handlers using **business keys** or **event IDs**.

#### Easy mistakes

- Assuming **global order** across partitions.  
- **Slow consumer** → lag; **poison message** blocks partition without **skip/DLQ** strategy.  
- **Fire-and-forget** publish with no **outbox** when DB + event must align.

#### Quick checks

- [ ] **Partition count** vs **consumer count** rule.  
- [ ] Why **compacted** topic vs **retention** topic.  
- [ ] **Rebalancing** pain — **sticky assignor** / **cooperative** at high level.

1️⃣ What is Kafka?
Apache Kafka is a distributed streaming platform that can:

Publish and subscribe to streams of records (like a message broker).

Store streams of records durably.

Process streams of records in real-time.

Core Use-Cases:

Event-driven architecture

Log aggregation

Messaging queues replacement

Real-time analytics / streaming pipelines

Example:

E-Commerce: When a user places an order → Kafka Topic: order_created → consumed by Inventory MS, Payment MS, Notification MS.

2️⃣ Core Concepts
Concept	Description
Producer	Application/service that publishes messages to a Kafka topic.
Consumer	Application/service that reads messages from a Kafka topic.
Topic	Category or feed name to which records are published.
Partition	Topics are divided into partitions → enables parallelism.
Offset	Unique identifier of a record in a partition. Consumers track offsets.
Broker	Kafka server that stores messages and serves clients.
Cluster	Collection of brokers for fault-tolerance and scalability.
Consumer Group	A group of consumers that share reading of a topic (load balancing).
3️⃣ Kafka Architecture
          ┌───────────────┐
          │   Producer    │
          └───────┬───────┘
                  │
                  ▼
           ┌───────────────┐
           │   Kafka Topic │
           │  Partitions   │
           └─────┬─────────┘
  ┌──────────────┼──────────────┐
  ▼              ▼              ▼
Partition 0   Partition 1   Partition 2
  │              │              │
  ▼              ▼              ▼
┌─────┐       ┌─────┐        ┌─────┐
│Broker│       │Broker│        │Broker│
└─────┘       └─────┘        └─────┘
  │              │              │
  ▼              ▼              ▼
┌───────────────┐
│ Consumer Group│
│  (Consumers)  │
└───────────────┘
Notes:

Each partition is ordered, but Kafka doesn’t guarantee ordering across partitions.

Producers can specify key → ensures messages with same key go to same partition.

Consumer groups enable horizontal scaling: multiple consumers read from the same topic in parallel.

4️⃣ How Kafka Works Internally
4.1 Producer → Broker Flow
Producer sends a message → broker

Broker appends message to the log (persistent, sequential)

Broker returns acknowledgment (configurable: none, leader, all)

4.2 Consumer → Broker Flow
Consumer polls messages from broker

Tracks offset (can be auto-commit or manual commit)

Can re-read old messages using offset → useful for reprocessing events

4.3 Partitioning
Each topic has N partitions → allows parallel processing.

Messages with same key always go to same partition → ensures order per key.

4.4 Replication & Fault Tolerance
Each partition has leader + followers

Leader handles all reads/writes; followers replicate

If leader fails → a follower becomes the new leader

5️⃣ Kafka Guarantees
Guarantee	Description
Durability	Messages written to disk → survive broker restarts
Ordering	Guaranteed per partition, not across partitions
At-least-once	Default; messages may be delivered multiple times
Exactly-once	With idempotent producers & transactions (Kafka 0.11+)
High-throughput	Handles millions of messages/sec
6️⃣ Kafka Use-Cases (Real-World)
Event-driven microservices

E.g., order_created triggers Inventory, Payment, Notification services asynchronously.

Log aggregation

Collect logs from multiple servers → send to central storage (ElasticSearch, S3)

Metrics & monitoring

High-volume events → real-time dashboards

Stream processing

Kafka + Spark / Flink → real-time analytics pipelines

Data pipelines

Kafka → ETL pipelines → Snowflake / Redshift / MongoDB

7️⃣ Kafka Producer / Consumer Code Snippets (Java)
Producer
Properties props = new Properties();
props.put("bootstrap.servers", "localhost:9092");
props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

KafkaProducer<String, String> producer = new KafkaProducer<>(props);

ProducerRecord<String, String> record =
        new ProducerRecord<>("order_created", "order123", "Order details");

producer.send(record, (metadata, exception) -> {
    if (exception != null) exception.printStackTrace();
    else System.out.println("Sent: " + metadata.partition() + " offset: " + metadata.offset());
});

producer.close();
Consumer
Properties props = new Properties();
props.put("bootstrap.servers", "localhost:9092");
props.put("group.id", "order-service");
props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
props.put("enable.auto.commit", "false");

KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);
consumer.subscribe(Arrays.asList("order_created"));

while(true) {
    ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100));
    for (ConsumerRecord<String, String> record : records) {
        System.out.printf("Received: key=%s, value=%s, offset=%d%n", 
                          record.key(), record.value(), record.offset());
    }
    consumer.commitSync(); // manual commit
}
8️⃣ Kafka Advanced Patterns
Topic per microservice

Avoids tight coupling between services

Dead-letter topic

Handle messages that fail processing

Compacted topics

Only keep the latest event per key (useful for state events)

Exactly-once semantics

Idempotent producer + transactional consumer

Multi-region replication

Disaster recovery & global scale

9️⃣ Interview-Level Questions on Kafka
Explain partitioning and message ordering in Kafka.

How does Kafka achieve high availability?

Difference between at-least-once, at-most-once, and exactly-once delivery.

How would you design a notification system using Kafka?

Kafka vs RabbitMQ / traditional MQ → when to use what?

How do consumer groups scale your system horizontally?

Explain log compaction and retention policies.

How to handle message reprocessing and offsets?

What are dead-letter queues and why are they important?

How would you monitor Kafka in production (metrics, lag, errors)?

💡 SDE-2 Key Takeaways:

Kafka is core to event-driven microservices and stream processing pipelines.

Understanding partitioning, replication, consumer groups, and delivery semantics is critical.

Interviewers love designing async pipelines using Kafka for scalability and fault tolerance.

Producer → Topic → Partition → Brokers → Consumer Groups → Jobs / Async Processing, including retry, dead-letter queue, and monitoring—perfect for interviews.


---

_Architecture diagram (ASCII):_


please draw the diagram


Kafka System Architecture Diagram
                   ┌───────────────┐
                   │   Producer    │
                   │ (Microservice)│
                   └───────┬───────┘
                           │
                  ┌────────┴─────────┐
                  │   Kafka Topic    │
                  │  "order_created" │
                  └────────┬─────────┘
           ┌──────────────┼───────────────┐
           ▼              ▼               ▼
    ┌────────────┐ ┌────────────┐ ┌────────────┐
    │ Partition0 │ │ Partition1 │ │ Partition2 │
    │ Leader +   │ │ Leader +   │ │ Leader +   │
    │ Followers  │ │ Followers  │ │ Followers  │
    └──────┬─────┘ └─────┬──────┘ └─────┬─────┘
           │               │               │
           ▼               ▼               ▼
    ┌────────────┐ ┌────────────┐ ┌────────────┐
    │ Consumer0  │ │ Consumer1  │ │ Consumer2  │
    │ (Service)  │ │ (Service)  │ │ (Service)  │
    └──────┬─────┘ └─────┬──────┘ └─────┬─────┘
           │               │               │
           ▼               ▼               ▼
     ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
     │ Offset store│ │ Retry Topic │ │ DLQ Topic   │
     │ (Zookeeper /│ │ "order_retry"│ │ "order_dlq"│
     │ Kafka)      │ │             │ │             │
     └─────────────┘ └─────────────┘ └─────────────┘
           │
           ▼
     ┌─────────────┐
     │ Monitoring  │
     │ Prometheus  │
     │ Grafana /   │
     │ Kafka Manager│
     └─────────────┘
Flow Explanation
Producer

Publishes events (e.g., order_created) → Kafka Topic

Can specify key → ensures same key goes to same partition (ordering).

Topic & Partitions

Topic is divided into multiple partitions → allows parallel processing.

Each partition has leader + followers → replication ensures fault tolerance.

Consumer Groups

Consumers in a group read partitions in parallel → horizontal scaling.

Tracks offsets for reprocessing.

Retries and Dead-Letter Queue (DLQ)

Failed messages → moved to retry topic

Messages that fail multiple times → moved to DLQ for manual investigation.

Offset Store

Kafka / Zookeeper stores committed offsets

Enables replay of messages for debugging or recovery.

Monitoring

Track consumer lag, partition health, throughput, broker metrics.

Tools: Prometheus + Grafana, Kafka Manager, ELK Stack.

Interview Key Points
Partitioning & ordering → discuss how key-based partitioning guarantees order per key.

Replication → leader + followers → high availability.

Consumer groups → horizontal scaling & load balancing.

DLQs & retries → ensure no messages are lost while avoiding blocking main pipeline.

Monitoring → critical in production for latency, lag, and failures.

💡 With this diagram and explanation, you can explain Kafka architecture end-to-end in interviews, covering async pipelines, retries, fault tolerance, and monitoring.

## Interview questions, mocks & scenarios

please answer the questions


1️⃣ Explain partitioning and message ordering in Kafka.
Answer:

Each topic is divided into partitions.

Producers can specify a key → all messages with the same key go to the same partition.

Ordering guarantee:

Within a partition: Messages are strictly ordered by offset.

Across partitions: No ordering guarantee.

Use case: For an e-commerce system, all messages for the same order (orderId) go to the same partition to preserve order.

2️⃣ How does Kafka achieve high availability?
Answer:

Kafka uses replication of partitions:

Each partition has a leader + followers.

Leader handles all reads/writes; followers replicate.

Leader failure: One follower is promoted as leader.

Distributed cluster → multiple brokers → horizontal scaling.

Can tolerate broker failures without losing messages (replication factor ≥ 2 or 3).

3️⃣ Difference between at-least-once, at-most-once, and exactly-once delivery.
Semantics	Behavior	Use Case
At-least-once	Message may be delivered more than once.	Safe for critical messages, idempotent consumers required.
At-most-once	Message may be lost, but never duplicated.	Non-critical notifications.
Exactly-once	Message delivered once and only once, using idempotent producers + transactional consumers.	Payment transactions, financial systems.
4️⃣ How would you design a notification system using Kafka?
Answer:

Producer: Microservices publish events (order_created, profile_updated).

Topic: notifications.

Consumer Group: Multiple notification services (email, SMS, push).

Flow:

Producer → Kafka Topic

Consumer → Reads event → Sends notification

Retry failed notifications → Use dead-letter queue

Benefits: Async, scalable, fault-tolerant.

5️⃣ Kafka vs RabbitMQ / traditional MQ → when to use what?
Feature	Kafka	RabbitMQ / MQ
Messaging model	Pub/Sub / Streaming	Queue / Pub-Sub
Persistence	Disk-based, durable	In-memory / Disk
Throughput	High (millions/sec)	Medium
Ordering	Per partition	Guaranteed per queue
Consumer model	Pull-based	Push-based
Use case	Event-driven systems, real-time analytics	Request/response, task queue
Rule:

Use Kafka for high-throughput streaming, decoupled microservices, async pipelines.

Use RabbitMQ for low-volume, reliable, ordered task queues.

6️⃣ How do consumer groups scale your system horizontally?
Answer:

Consumer group: Multiple consumers share reading from a topic.

Each partition is consumed by only one consumer per group.

Horizontal scaling: Add more consumers → Kafka distributes partitions → parallel processing.

Example: 10 partitions + 5 consumers → 2 partitions per consumer.

7️⃣ Explain log compaction and retention policies.
Log retention:

Kafka deletes messages older than a retention time or when disk quota is exceeded.

Log compaction:

Kafka keeps latest message per key and discards older ones.

Useful for stateful events (user profile updates).

Benefit: Prevents unbounded storage growth while preserving current state.

8️⃣ How to handle message reprocessing and offsets?
Answer:

Kafka stores offsets per partition.

Manual commit: Consumer decides when to commit → can re-read messages on failure.

Automatic commit: Kafka commits offsets periodically → risk of duplicate processing.

Example: Reprocessing all order_created events → reset consumer offset to earliest.

9️⃣ What are dead-letter queues (DLQ) and why are they important?
Answer:

DLQ: Separate Kafka topic to store messages that failed processing multiple times.

Benefits:

Prevents blocking the main topic

Enables debugging/failure analysis

Helps implement retries with backoff

10️⃣ How would you monitor Kafka in production?
Answer:

Metrics to monitor:

Broker health (CPU, memory, disk usage)

Under-replicated partitions

Consumer lag (messages waiting to be consumed)

Message throughput and latency

Request/response errors

Tools: Prometheus + Grafana, Kafka Manager, Confluent Control Center, ELK stack

Alerting: Trigger alerts when consumer lag exceeds threshold or brokers are down.

✅ SDE-2 Key Takeaways for Interviews:

Kafka is central to event-driven architectures.

Must understand partitions, replication, offsets, consumer groups, and delivery semantics.

Be ready to design async pipelines, including retries, DLQ, monitoring, and exactly-once processing.

Producers → Topics → Partitions → Brokers → Consumer Groups → DLQs → Monitoring, which is perfect for interview discussion and explanation.
