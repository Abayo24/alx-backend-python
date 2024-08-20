#!/usr/bin/env python3
"""Async Comprehensions"""


import asyncio
import random
from typing import AsyncGenerator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> AsyncGenerator[float, None]:
    """
    collect 10 random numbers using an async
    comprehensing over async_generator
    """
    random_num = [i async for i in async_generator()]
    print(random_num)
