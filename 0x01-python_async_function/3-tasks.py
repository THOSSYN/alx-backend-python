#!/usr/bin/env python3
""" An asynchronous programming in python"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ A function that returns task

        Args:
          max_delay (int): is the delay time

        Return (asyncio.Task): the tasks
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
