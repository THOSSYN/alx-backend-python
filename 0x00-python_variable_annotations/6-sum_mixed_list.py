#!/usr/bin/env python3
"""Type-annotated function sum_mixed_list"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """A function that adds elements of a list
      Args:
        mxd_lst (List[int | float]): list of int and float

      Return (float): the sum of all the items in mxd_lst
    """
    summation = 0

    for item in mxd_lst:
        summation += item
    return summation
