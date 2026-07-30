from collections import defaultdict, deque
import time
from typing import Dict

class SlidingWindowRateLimiter:
    def __init__(self, max_requests: int, window_seconds: float):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.logs: Dict[str, deque] = defaultdict(deque)

    def is_allowed(self, client_id: str, current_time: float = None) -> bool:
        now = current_time if current_time is not None else time.time()
        client_queue = self.logs[client_id]

        # Purge timestamps outside the window boundary
        boundary = now - self.window_seconds
        while client_queue and client_queue[0] <= boundary:
            client_queue.popleft()

        if len(client_queue) < self.max_requests:
            client_queue.append(now)
            return True

        return False
