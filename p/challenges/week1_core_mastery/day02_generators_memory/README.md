# Day 02: Memory-Efficient Log Streaming Generator

## 💡 Concept Overview
Backend engineers regularly deal with multi-gigabyte log files or network streams. Reading an entire file into memory using `.readlines()` can crash backend processes with out-of-memory (OOM) errors. Python generators provide lazy iteration, allowing data to be processed line by line in constant $O(1)$ memory space.

## 🎯 Backend Scenario
You need to parse massive production server access logs to isolate HTTP 5xx errors or slow requests (> 500ms response time).

Implement a generator pipeline in `starter.py` consisting of:
1. `stream_log_lines(lines_iterable)`: Yields non-empty stripped log lines.
2. `parse_log_entry(line)`: Parses formatted string `"TIMESTAMP LEVEL ENDPOINT STATUS_CODE RESPONSE_TIME_MS"`.
3. `filter_log_events(parsed_stream, level=None, min_status=None, min_duration_ms=None)`: Filters entries lazily.

## 🛠️ Instructions
1. Implement the generator functions in `starter.py`.
2. Test your solution:
   ```bash
   python daily_push.py --test 2
   ```
3. Complete and push:
   ```bash
   python daily_push.py --complete 2
   ```
