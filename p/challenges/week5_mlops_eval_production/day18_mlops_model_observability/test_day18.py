import pytest
from challenges.week5_mlops_eval_production.day18_mlops_model_observability.solution import LLMObservabilityTracer

def test_llm_observability_tracing():
    tracer = LLMObservabilityTracer()
    t1 = tracer.trace_call(
        model_name="gpt-4o",
        prompt="Explain FastAPI dependency injection",
        completion="FastAPI uses Depends() for DI.",
        duration_ms=250.0
    )

    assert t1["prompt_tokens"] > 0
    assert t1["total_tokens"] > 0
    assert t1["estimated_cost_usd"] > 0.0

    t2 = tracer.trace_call(
        model_name="gpt-4o",
        prompt="Explain Pydantic validation",
        completion="Pydantic validates types at runtime.",
        duration_ms=150.0
    )

    metrics = tracer.get_aggregated_metrics()
    assert metrics["total_calls"] == 2
    assert metrics["avg_duration_ms"] == 200.0
