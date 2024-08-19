#!/usr/bin/env python3
"""Function that  measures the total execution time for wait_n"""


import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time_async(n: int, max_delay: int) -> float:
    """measure_time function returns returns total_time / n"""
    my_time = time.perf_counter()
    await wait_n(n, max_delay)
    total_time = time.perf_counter() - my_time
    return total_time / n


def measure_time(n: int, max_delay: int) -> float:
    """"""
    return asyncio.run(measure_time_async(n, max_delay))
