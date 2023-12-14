#!/usr/bin/env python3
"""Write a coroutine called async_generator that takes no arguments"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """  loop 10 times, each time asynchronously wait 1 second """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
