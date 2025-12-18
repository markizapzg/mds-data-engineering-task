# MDS Data Engineer – Python Task

This repository contains a Python implementation of the data engineering task
for MDS Informatički inženjering.

The solution focuses on clean system modeling, concurrency, testability,
and extensibility using **pure Python** and standard libraries only.

---

## Overview

The project consists of two independent processing pipelines:

1. **Streaming message processing with time-based minibatching**
2. **Nightly file processing with size-based bucketing**

An optional bonus task is also included and clearly isolated from the core solution.

---

## 1. Streaming Minibatching

### Problem
- Messages arrive following a Poisson distribution (~10 messages per minute).
- A minibatch is created when the first message arrives.
- All messages arriving within the next **5 minutes** are added to that minibatch.
- Once the minibatch window closes, it is sent for processing.
- New minibatches must not wait for previous ones to finish processing.
- Processing is done using a worker pool with **10 threads**.

### Solution
- A `MiniBatchManager` manages the lifecycle of minibatches.
- The first message opens a minibatch.
- A `threading.Timer` is used to close the minibatch after a fixed duration.
- Completed minibatches are submitted asynchronously to a shared worker pool.
- Concurrency is handled using `threading.Lock` to ensure thread safety.

This approach models event-time batching behavior without introducing external
streaming frameworks.

---

## 2. Nightly File Processing and Bucketing

### Problem
- 100 files arrive nightly for processing.
- File sizes follow an exponential distribution.
- Processing small files individually is inefficient.
- Files should be grouped into buckets of **maximum 10MB** before processing.
- Bucketing strategy should be easy to replace or extend.

### Solution
- Files are represented as simple data objects.
- Buckets accumulate files until the size limit is reached.
- A `BucketingStrategy` interface is used to decouple bucketing logic.
- A simple sequential bucketing strategy is provided as a concrete implementation.
- Buckets are submitted to the same shared worker pool used by the streaming pipeline.

This design follows SOLID principles and allows alternative bucketing strategies
to be introduced with minimal changes.

---

## Project Structure

```text
src/
  messaging/    # Streaming minibatching logic
  files/        # File bucketing and processing
  workers/      # Shared worker pool
  bonus/        # Optional bonus task (isolated)
tests/          # Unit tests

```

### Testing

Unit tests are provided for:

- Minibatch lifecycle and closing behavior
- File bucketing size constraints
- Worker pool submission

Tests can be executed locally using:

```bash
PYTHONPATH=. python3 -m pytest -v
```
Docker

The project is dockerized to allow easy and reproducible testing.

```bash
Build and run:

docker build -t mds-task .
docker run mds-task
```
The container runs the test suite by default.

### Bonus

An optional bonus solution is available in src/bonus/.

It demonstrates a heuristic approach to tournament scheduling and player rotation.
The bonus is intentionally isolated from the core task and does not affect
the main solution.

### Notes

The solution uses only standard Python libraries
The focus is on clarity, extensibility, and correctness rather than optimal algorithms
External frameworks (Kafka, Spark, Airflow, etc.) were intentionally avoided
to keep the implementation lightweight and easy to reason about


The focus is on clarity, extensibility, and correctness rather than optimal algorithms.

External frameworks (Kafka, Spark, Airflow, etc.) were intentionally avoided
to keep the implementation lightweight and easy to reason about.
