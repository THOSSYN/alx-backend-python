#!/usr/bin/env python3
"""A type-annotated function"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ A function that return its arguments as tuple

      Args:
        k (str): first argument
        v (int or float): second argumet

      Return: tuple of int and float
    """
    return tuple([k, float(v ** 2)])
