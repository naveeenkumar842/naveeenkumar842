# Day 04: Transactional Context Manager & Resource Guard

## 💡 Concept Overview
Context managers (`with` statements) in Python guarantee resource cleanup (closing DB connections, releasing locks, clearing temporary tables) regardless of whether execution succeeds or raises an unhandled exception.

## 🎯 Backend Scenario
You are designing a database unit-of-work pattern for financial transactions.
Build `DatabaseTransactionGuard` (supporting both class `__enter__`/`__exit__` and `@contextmanager` generator patterns):
1. `__enter__`: Begins transaction, logs start time, returns transaction object.
2. `__exit__`:
   - If an exception occurs: triggers automatic `rollback()`, logs exception info, and suppresses exception if `suppress_errors=True`.
   - If execution succeeds: calls `commit()` and records execution metadata.

## 🛠️ Instructions
1. Implement the context manager in `starter.py`.
2. Test your solution:
   ```bash
   python daily_push.py --test 4
   ```
3. Complete and push:
   ```bash
   python daily_push.py --complete 4
   ```
