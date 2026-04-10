#!/usr/bin/env python3
"""Run multiple async tasks and return their results."""
from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Launch n tasks and return delays in order of completion."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    results = []
    for task in asyncio.as_completed(tasks):
        results.append(await task)

    return results