#!/usr/bin/env python3
"""
Multiple coroutines execution
"""
import importlib
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays"""
    result: List = [await wait_random(max_delay) for _ in range(n)]
    for i in range(0, len(result)):
        for j in range(i + 1, len(result)):
            if result[i] >= result[j]:
                temp = result[i]
                result[i] = result[j]
                result[j] = temp
    return result
