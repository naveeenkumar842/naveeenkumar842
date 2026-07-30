import asyncio
from typing import List, Dict, Any, Optional

async def bounded_fetch(
    task_id: int,
    mock_delay: float,
    semaphore: asyncio.Semaphore,
    fail_on: Optional[List[int]] = None
) -> Dict[str, Any]:
    """
    Executes a task bounded by an asyncio.Semaphore.
    """
    async with semaphore:
        await asyncio.sleep(mock_delay)
        if fail_on and task_id in fail_on:
            raise RuntimeError(f"Task {task_id} failed simulation")
        return {"id": task_id, "status": "COMPLETED", "delay": mock_delay}

async def process_batch_concurrently(
    tasks: List[Dict[str, Any]],
    max_concurrency: int
) -> Dict[str, List[Any]]:
    """
    Executes tasks concurrently bounded by max_concurrency.
    """
    semaphore = asyncio.Semaphore(max_concurrency)
    coros = [
        bounded_fetch(
            task_id=task["id"],
            mock_delay=task.get("delay", 0.01),
            semaphore=semaphore,
            fail_on=task.get("fail_on")
        )
        for task in tasks
    ]

    results = await asyncio.gather(*coros, return_exceptions=True)

    successful = []
    failed = []

    for res in results:
        if isinstance(res, Exception):
            failed.append(str(res))
        else:
            successful.append(res)

    return {"successful": successful, "failed": failed}
