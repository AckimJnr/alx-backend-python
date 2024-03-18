#!/usr/bin/env python3
"""
module: 0-basic_async_syntax
"""

import asyncio
import random


async def wait_random(max_delay=10):
    """
    generates a random delay
    max_delay: maximum delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay