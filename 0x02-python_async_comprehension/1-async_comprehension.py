#!/usr/bin/env python3
""" The coroutine will collect 10 random numbers
using an async comprehensing over async_generator,
then return the 10 random numbers. """

from typing import List


async def async_comprehension() -> List[float]:
    # Using async comprehension to collect 10 random numbers
    random_numbers = [value async for value in async_generator()]
    return random_numbers
