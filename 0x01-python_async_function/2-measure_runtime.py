#!/usr/bin/env python3
"""
module: 2-measure_runtime
"""

import asyncio
import time
from typing import Callable, List


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    calculates the amount of time the function
    took to complete execution
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
