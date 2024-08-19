#!/usr/bin/env python3
"""
Multiple coroutines execution
"""
import importlib
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List:
    """return the list of all the delays"""
    result = [await wait_random(max_delay) for _ in range(n)]
    return result
