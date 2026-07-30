# Day 03: AsyncIO Concurrency & Semaphore Bounded Worker Pool

## 💡 Concept Overview
AsyncIO is a core building block for high-throughput Python backends (FastAPI, Tornado, Sanic). When executing hundreds of asynchronous tasks concurrently (e.g. fetching third-party APIs or database queries), an unbounded `asyncio.gather` can overwhelm target servers or exhaust connection pools.

Using `asyncio.Semaphore`, engineers limit concurrent operations to a safe maximum bound.

## 🎯 Backend Scenario
Build a concurrent batch task processor:
1. `bounded_fetch(task_id, mock_delay, semaphore, fail_on=None)`: Simulates an async network call bounded by `asyncio.Semaphore`.
2. `process_batch_concurrently(tasks, max_concurrency)`: Runs all tasks concurrently using `asyncio.gather` with `return_exceptions=True`. Returns `{"successful": [...], "failed": [...]}`.

## 🛠️ Instructions
1. Implement the async functions in `starter.py`.
2. Run tests:
   ```bash
   python daily_push.py --test 3
   ```
3. Complete and push:
   ```bash
   python daily_push.py --complete 3
   ```
