#!/usr/bin/env python3
"""
Multiple coroutines execution
"""
import importlib
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays"""
    result: List[float] = [await task_wait_random(max_delay) for _ in range(n)]
    for i in range(0, len(result)):
        for j in range(i + 1, len(result)):
            if result[i] >= result[j]:
                temp = result[i]
                result[i] = result[j]
                result[j] = temp
    return result
