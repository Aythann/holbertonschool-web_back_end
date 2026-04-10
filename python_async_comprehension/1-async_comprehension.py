#!/usr/bin/env python3
"""Module contenant une compréhension asynchrone."""


from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random float values using an async comprehension."""
    return [value async for value in async_generator()]
