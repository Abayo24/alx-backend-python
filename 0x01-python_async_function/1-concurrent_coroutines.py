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
    delays = []
    for delay in await asyncio.gather(*(wait_random(max_delay) for _ in range(n))):
        # Insert the delay into the sorted position
        i = 0
        while i < len(delays) and delays[i] < delay:
            i += 1
        delays.insert(i, delay)
    return delays
