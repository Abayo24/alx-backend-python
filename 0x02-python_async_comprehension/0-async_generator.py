#!/usr/bin/env python3
""" coroutine called async_generator that takes no arguments."""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, float]:
    """
    loop 10 times, each time asynchronously
    wait 1 second, then yield a random number
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
