#!/usr/bin/env python3
"""async comprehension and annotations"""


from typing import List
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Using async comprehension to collect 10 random numbers"""
    random_num: List[float] = [i async for i in async_generator()]
    return random_num
