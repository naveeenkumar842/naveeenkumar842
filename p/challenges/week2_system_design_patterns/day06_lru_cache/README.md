# Day 06: O(1) LRU Cache (Doubly Linked List + Hash Map)

## 💡 Concept Overview
Least Recently Used (LRU) Caching is a foundational system design pattern used in Redis, database buffer pools, and web framework memoization. An LRU Cache must support `get(key)` and `put(key, value)` in $O(1)$ constant time complexity.

## 🎯 Backend Scenario
Implement a thread-safe / clean `LRUCache` class with fixed `capacity`:
1. `get(key)`: Returns value if key exists, updating node to Most Recently Used (MRU) head position. Returns `-1` (or `None`) if key missing.
2. `put(key, value)`: Inserts or updates key. If capacity is exceeded, evicts the Least Recently Used (LRU) tail node in $O(1)$ time.

## 🛠️ Instructions
1. Implement `LRUCache` using a custom Doubly Linked List + Dictionary in `starter.py`.
2. Test your solution:
   ```bash
   python daily_push.py --test 6
   ```
3. Complete and push:
   ```bash
   python daily_push.py --complete 6
   ```
