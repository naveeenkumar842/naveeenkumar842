# Day 07: Sliding Window Log Rate Limiter

## 💡 Concept Overview
API Rate Limiting prevents Denial of Service (DoS) attacks, brute-force requests, and resource overuse. The Sliding Window Log algorithm tracks precise timestamps of incoming requests per client IP / API key within a configurable window (e.g. 5 requests per 10 seconds).

## 🎯 Backend Scenario
Build `SlidingWindowRateLimiter`:
1. Constructor accepts `max_requests: int` and `window_seconds: float`.
2. `is_allowed(client_id: str, current_time: float) -> bool`:
   - Purges timestamps older than `current_time - window_seconds`.
   - If remaining timestamps count < `max_requests`, records `current_time` and returns `True`.
   - Otherwise, returns `False`.

## 🛠️ Instructions
1. Implement in `starter.py`.
2. Test your solution:
   ```bash
   python daily_push.py --test 7
   ```
3. Complete and push:
   ```bash
   python daily_push.py --complete 7
   ```
