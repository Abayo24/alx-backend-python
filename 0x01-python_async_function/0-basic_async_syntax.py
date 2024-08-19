#!/usr/bin/env python3
"""
asynchronous coroutine that takes in an integer
that waits for a random delay and returns it
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> int:
    """asynchronous coroutine"""
    return random.uniform(0, max_delay)
