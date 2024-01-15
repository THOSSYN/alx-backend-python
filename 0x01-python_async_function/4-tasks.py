#!/usr/bin/env python3
"""A python asynchronous programming basic"""

import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ A function that calls wait_random n times
        with specified max_delay

        Args:
          n (int): number of times to spawn wait_random()
          max_delay (int): specifies upper limit for which
          random module generates delay

        Return List[float]: A list of all delay value
    """
    result = await asyncio.gather(
            *(task_wait_random(max_delay) for i in range(n)))
    return list(sorted(result))
