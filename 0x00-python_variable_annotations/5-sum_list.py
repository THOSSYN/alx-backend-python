#!/usr/bin/env python3
"""Type-annotated function"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """A function that adds up the elements of a list

       Args:
           input_list (list[float]): Argument to function

       Return (float): The sum of elements of the input_list
    """
    summation = 0

    for item in input_list:
        summation += item
    return summation
