#!/usr/bin/env python3
"""
module: 3-tasks
"""
import asyncio
from random import uniform

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    try returning a Task type
    """
    loop = asyncio.get_running_loop()
    task = loop.create_task(wait_random(max_delay))
    return task
