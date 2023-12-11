#!/usr/bin/env python3
"""Python async"""


import asyncio
import random


async def wait_random(max_delay=10):
    """waits for a random delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay