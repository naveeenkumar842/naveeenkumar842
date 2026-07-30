import functools
import time
from typing import Callable, Any, Optional

RAISE_EXCEPTION = object()

def telemetry_guard(
    retries: int = 0,
    log_args: bool = True,
    on_error_return: Any = RAISE_EXCEPTION
) -> Callable:
    """
    Decorator for tracking metrics, timing execution, and handling retries/errors.
    """
    def decorator(func: Callable) -> Callable:
        stats = {
            "call_count": 0,
            "total_duration_ms": 0.0,
            "last_exception": None,
            "retries_count": 0
        }

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            stats["call_count"] += 1
            start_time = time.perf_counter()
            attempts = 0

            while attempts <= retries:
                try:
                    result = func(*args, **kwargs)
                    duration_ms = (time.perf_counter() - start_time) * 1000
                    stats["total_duration_ms"] += duration_ms
                    return result
                except Exception as e:
                    attempts += 1
                    stats["last_exception"] = str(e)
                    if attempts <= retries:
                        stats["retries_count"] += 1
                        continue

                    if on_error_return is not RAISE_EXCEPTION:
                        duration_ms = (time.perf_counter() - start_time) * 1000
                        stats["total_duration_ms"] += duration_ms
                        return on_error_return
                    raise

        wrapper._telemetry_stats = stats
        return wrapper
    return decorator
