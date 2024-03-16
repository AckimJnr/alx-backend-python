#!/usr/bin/env python3
"""
module: 9-element_length
Contains a function element_length that return sthe length of an element
"""
from typing import List, Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns the lenght of a list
    Args:
        lst: The list to be checked

    Returns:
        Int: Lenth of the list
    """
    return [(i, len(i)) for i in lst]
