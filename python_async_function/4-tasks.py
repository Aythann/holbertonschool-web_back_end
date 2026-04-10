#!/usr/bin/env python3
"""Module defining a coroutine that runs multiple tasks concurrently."""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times and
	return the delays in ascending order."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task
        delays.append(delay)

    return delays
