from collections import defaultdict, deque
import time
from typing import Dict

class SlidingWindowRateLimiter:
    def __init__(self, max_requests: int, window_seconds: float):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.logs: Dict[str, deque] = defaultdict(deque)

    def is_allowed(self, client_id: str, current_time: float = None) -> bool:
        # TODO: Implement sliding window timestamp purging and request check
        pass
