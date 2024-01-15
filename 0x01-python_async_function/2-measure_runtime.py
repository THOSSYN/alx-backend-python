#!/usr/bin/env python3
""" An asynchronous python programming script"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ A function that measures total time taking
        for a pool of request to run

        Args:
          n (int): the number of times a function runs
          max_delay (int): the waiting time

        Return: total_time per n
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter() - start_time
    return end_time / n
