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
    result = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return result
