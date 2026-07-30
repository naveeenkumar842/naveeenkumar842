import math
from typing import Dict, Any, List

# Cost per 1K tokens mock
MODEL_PRICING = {
    "gpt-4o": {"input": 0.005, "output": 0.015},
    "default": {"input": 0.001, "output": 0.002}
}

class LLMObservabilityTracer:
    def __init__(self):
        self.traces: List[Dict[str, Any]] = []

    def estimate_token_count(self, text: str) -> int:
        """Estimates token count (~4 characters per token)."""
        if not text:
            return 0
        return max(1, math.ceil(len(text) / 4.0))

    def trace_call(
        self,
        model_name: str,
        prompt: str,
        completion: str,
        duration_ms: float
    ) -> Dict[str, Any]:
        prompt_tokens = self.estimate_token_count(prompt)
        completion_tokens = self.estimate_token_count(completion)
        total_tokens = prompt_tokens + completion_tokens

        pricing = MODEL_PRICING.get(model_name.lower(), MODEL_PRICING["default"])
        cost = (prompt_tokens / 1000.0 * pricing["input"]) + (completion_tokens / 1000.0 * pricing["output"])

        trace = {
            "model": model_name,
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": total_tokens,
            "duration_ms": duration_ms,
            "estimated_cost_usd": round(cost, 6)
        }
        self.traces.append(trace)
        return trace

    def get_aggregated_metrics(self) -> Dict[str, Any]:
        if not self.traces:
            return {
                "total_calls": 0,
                "total_tokens": 0,
                "avg_duration_ms": 0.0,
                "total_cost_usd": 0.0
            }

        total_calls = len(self.traces)
        total_tokens = sum(t["total_tokens"] for t in self.traces)
        total_duration = sum(t["duration_ms"] for t in self.traces)
        total_cost = sum(t["estimated_cost_usd"] for t in self.traces)

        return {
            "total_calls": total_calls,
            "total_tokens": total_tokens,
            "avg_duration_ms": round(total_duration / total_calls, 2),
            "total_cost_usd": round(total_cost, 6)
        }
