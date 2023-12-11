#!/usr/bin/env python3
"""wait_n to task_wait_n"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delay = await asyncio.gather(*tasks)
    return delay
