#!/usr/bin/env python3
"""Annotating ready-made function"""

from typing import Optional, Tuple, List, Union


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """A function that returns a tuple"""
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)
