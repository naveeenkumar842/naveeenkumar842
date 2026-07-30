from typing import Any, Optional

class Node:
    def __init__(self, key: Any = None, val: Any = None):
        self.key = key
        self.val = val
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # TODO: Initialize hash map and dummy head/tail nodes for doubly linked list
        pass

    def get(self, key: Any) -> Any:
        # TODO: Return value and move node to head (MRU)
        pass

    def put(self, key: Any, value: Any) -> None:
        # TODO: Insert/Update node and evict tail (LRU) if capacity exceeded
        pass
