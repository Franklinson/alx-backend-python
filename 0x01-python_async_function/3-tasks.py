#!/usr/bin/env python3
"""take an int and return an asyncio value"""


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """return an asyncio task value"""
    return asyncio.create_task(wait_random(max_delay))
