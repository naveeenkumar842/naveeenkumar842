import pytest
from challenges.week2_system_design_patterns.day07_rate_limiter.solution import SlidingWindowRateLimiter

def test_rate_limiter_allows_up_to_max():
    limiter = SlidingWindowRateLimiter(max_requests=3, window_seconds=10.0)
    client = "user_123"

    assert limiter.is_allowed(client, current_time=100.0) is True
    assert limiter.is_allowed(client, current_time=101.0) is True
    assert limiter.is_allowed(client, current_time=102.0) is True
    # 4th request within 10s should be blocked
    assert limiter.is_allowed(client, current_time=103.0) is False

def test_rate_limiter_sliding_window_expiration():
    limiter = SlidingWindowRateLimiter(max_requests=2, window_seconds=5.0)
    client = "user_456"

    assert limiter.is_allowed(client, current_time=10.0) is True
    assert limiter.is_allowed(client, current_time=12.0) is True
    assert limiter.is_allowed(client, current_time=13.0) is False

    # After t=15.1, t=10.0 request is expired out of window
    assert limiter.is_allowed(client, current_time=15.1) is True
