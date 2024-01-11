#!/usr/bin/env python3
"""A type-annotated function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A function that returns a multiplier function

       Args:
         multiplier (float): first argument

       Return (Callable): a function 'multiplier'
    """
    return lambda x: x * multiplier
