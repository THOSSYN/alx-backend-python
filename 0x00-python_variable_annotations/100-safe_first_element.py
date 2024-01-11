#!/usr/bin/env python3

from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """A function that returns the first element of the sequence
       argument
    """
    if lst:
        return lst[0]
    else:
        return None
