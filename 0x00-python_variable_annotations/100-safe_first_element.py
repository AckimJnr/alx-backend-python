#!/usr/bin/env python3
"""
module: 100-safe_first_element
python ducktyping anotation
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """
    Returns the first element of a sequence
    if it exists, otherwise returns None.

    Args:
        lst (Sequence): A sequence of elements.

    Returns:
        Union[Any, None]: The first element of the
        sequence, or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
