#!/usr/bin/env python3
""" An asynchronous comprehension script"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ A function that uses asynchronous list
        comprehension for collecting result from a generator
    """
    result = [i async for i in async_generator()]
    return result
