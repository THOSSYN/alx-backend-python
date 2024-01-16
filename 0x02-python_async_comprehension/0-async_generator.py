#!/usr/bin/env python3
""" Asynchronous comprehension script"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ An async generator function that yields
        its result as it loops and repeats 10times

        Args: No argument

        Return Iterator[float]: yields the value it loops
        through one at a time
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
