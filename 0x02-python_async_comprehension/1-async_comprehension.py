#!/usr/bin/env python3
"""Async Comprehensions"""


import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collect 10 random numbers using an async
    comprehensing over async_generator
    """
    random_num = [i async for i in async_generator()]
    return random_num
