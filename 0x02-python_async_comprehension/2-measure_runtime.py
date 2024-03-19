#!/usr/bin/env python3
"""
module: 2-measure_runtime
"""
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure runtime of async functions
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
