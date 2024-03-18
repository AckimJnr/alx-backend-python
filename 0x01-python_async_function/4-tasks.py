#!/usr/bin/env python3
"""
module: 4-tasks.py
"""
import asyncio
from typing import List


task_wait_random = __import__('1-concurrent_coroutines').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    run functions sideby side
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)

    return sorted(results)
