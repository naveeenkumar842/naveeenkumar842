import pytest
from challenges.week2_system_design_patterns.day06_lru_cache.solution import LRUCache

def test_lru_cache_basic_operations():
    cache = LRUCache(2)
    cache.put(1, "A")
    cache.put(2, "B")
    assert cache.get(1) == "A"
    
    # Put 3 should evict 2 (since 1 was accessed via get(1))
    cache.put(3, "C")
    assert cache.get(2) == -1
    assert cache.get(3) == "C"
    assert cache.get(1) == "A"

def test_lru_cache_update_existing_key():
    cache = LRUCache(2)
    cache.put(1, 100)
    cache.put(2, 200)
    cache.put(1, 150) # Update key 1 value and move to MRU

    cache.put(3, 300) # Should evict key 2
    assert cache.get(2) == -1
    assert cache.get(1) == 150
    assert cache.get(3) == 300
