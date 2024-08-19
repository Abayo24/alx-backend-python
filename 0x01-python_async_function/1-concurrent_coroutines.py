#!/usr/bin/env python3
"""
Multiple coroutines execution
"""
import importlib
import asyncio


module_name = '0-basic_async_syntax'
module = importlib.import_module(module_name)
wait_random = module.wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """return the list of all the delays"""
    delays = []
    result = [await wait_random(max_delay) for _ in range(n)]
    for delay in result:
        i=0
        while i < len(delays) and delays[i] < delay:
            i+=1
        delays.insert(i, delay)
    return delays
