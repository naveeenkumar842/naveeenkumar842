import pytest
import asyncio
from challenges.week1_core_mastery.day03_asyncio_concurrency.solution import (
    process_batch_concurrently
)

def test_process_batch_concurrently_all_successful():
    tasks = [
        {"id": 1, "delay": 0.01},
        {"id": 2, "delay": 0.01},
        {"id": 3, "delay": 0.01}
    ]
    res = asyncio.run(process_batch_concurrently(tasks, max_concurrency=2))

    assert len(res["successful"]) == 3
    assert len(res["failed"]) == 0
    assert res["successful"][0]["id"] == 1

def test_process_batch_concurrently_with_failures():
    tasks = [
        {"id": 1, "delay": 0.01},
        {"id": 2, "delay": 0.01, "fail_on": [2]},
        {"id": 3, "delay": 0.01}
    ]
    res = asyncio.run(process_batch_concurrently(tasks, max_concurrency=3))

    assert len(res["successful"]) == 2
    assert len(res["failed"]) == 1
    assert "Task 2 failed simulation" in res["failed"][0]
