#!/usr/bin/env python3
""" A script that measures runtime for
   an asynchronous process
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ A function that measure the runtime of
       an asynchronous process repeating four times
    """
    start_time = time.perf_counter()
    result = await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter() - start_time
    return end_time
