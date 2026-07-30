# Day 18: MLOps LLM Observability, Token Counting & Tracing

## 💡 Concept Overview
LLM applications require real-time observability to monitor API latency, prompt/completion token usage, monetary cost calculation, and error rates (e.g. LangSmith, Phoenix, Arize).

## 🎯 Backend Scenario
Build `LLMObservabilityTracer`:
1. `trace_call(model_name: str, prompt: str, completion: str, duration_ms: float)`: Tracks invocation trace metadata.
2. `estimate_token_count(text: str) -> int`: Estimates token count using standard whitespace/sub-word ratio.
3. `get_aggregated_metrics() -> Dict[str, Any]`: Computes total tokens, total cost, average latency, and trace count.

## 🛠️ Instructions
1. Implement tracer in `starter.py`.
2. Test your solution:
   ```bash
   python daily_push.py --test 18
   ```
3. Complete and push:
   ```bash
   python daily_push.py --complete 18
   ```
