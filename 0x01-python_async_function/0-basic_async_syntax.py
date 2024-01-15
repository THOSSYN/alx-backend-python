#!/usr/bin/env python3
"""Asynchronous programming basic"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ A function that exemplifies how asynchronous
        programming works in basic

        Args:
          max_delay (int): A range for generating delay
          value with random module

        Return: the randomly generated delay value
    """
    waiting_time = random.uniform(0, max_delay)

    await asyncio.sleep(waiting_time)
    return waiting_time
