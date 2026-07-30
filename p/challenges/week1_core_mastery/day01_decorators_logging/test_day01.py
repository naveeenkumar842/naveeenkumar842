import pytest
import time
from challenges.week1_core_mastery.day01_decorators_logging.solution import (
    telemetry_guard,
    RAISE_EXCEPTION
)

def test_telemetry_guard_basic_execution():
    @telemetry_guard()
    def add(a: int, b: int) -> int:
        """Add two numbers."""
        return a + b

    assert add(2, 3) == 5
    assert add.__name__ == "add"
    assert add.__doc__ == "Add two numbers."
    assert add._telemetry_stats["call_count"] == 1

def test_telemetry_guard_retries_and_fallback():
    attempts = 0

    @telemetry_guard(retries=2, on_error_return="fallback_value")
    def flaky_func():
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            raise ValueError("Transient error")
        return "success"

    result = flaky_func()
    assert result == "success"
    assert attempts == 3
    assert flaky_func._telemetry_stats["retries_count"] == 2

def test_telemetry_guard_raise_on_exceeded_retries():
    @telemetry_guard(retries=1, on_error_return=RAISE_EXCEPTION)
    def failing_func():
        raise RuntimeError("Fatal system failure")

    with pytest.raises(RuntimeError):
        failing_func()

    assert failing_func._telemetry_stats["call_count"] == 1
    assert failing_func._telemetry_stats["last_exception"] == "Fatal system failure"
