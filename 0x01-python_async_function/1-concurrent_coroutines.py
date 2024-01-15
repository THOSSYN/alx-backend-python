#!/usr/bin/env python3
"""A python asynchronous programming basic"""

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ A function that calls wait_random n times
        with specified max_delay

        Args:
          n (int): number of times to spawn wait_random()
          max_delay (int): specifies upper limit for which
          random module generates delay

        Return List[float]: A list of all delay value
    """
    result = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return list(sorted(result))
