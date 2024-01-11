#!/usr/bin/env python3
"""Given a ready-made function, write an annotation"""

from typing import Sequence, Iterable, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """A function returns a tuple from its argument"""
    return [(i, len(i)) for i in lst]
