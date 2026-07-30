# Day 01: Advanced Decorators & Telemetry Guard

## 💡 Concept Overview
In Python backend development, decorators are essential for cross-cutting concerns such as logging, performance timing, rate limiting, authentication, and error telemetry.

## 🎯 Backend Scenario
You are building an API observability decorator for a microservice. You need to create a `@telemetry_guard` decorator that:
1. Accepts optional parameters: `retries` (default 0), `log_args` (default True), and `on_error_return` (default None).
2. Measures and records function execution time in milliseconds.
3. Automatically retries the wrapped function up to `retries` times if it raises an exception before falling back to `on_error_return` (or re-raising if `on_error_return` is `RAISE_EXCEPTION`).
4. Preserves function metadata (`__name__`, `__doc__`, signature) using `functools.wraps`.
5. Attaches a dictionary `_telemetry_stats` to the wrapped function object to inspect call count, total duration, and last exception.

## 🛠️ Instructions
1. Open `starter.py` and implement `telemetry_guard`.
2. Run tests to verify your implementation:
   ```bash
   python daily_push.py --test 1
   ```
3. Once tests pass, complete and push your solution:
   ```bash
   python daily_push.py --complete 1
   ```
