#!/usr/bin/env python3

"""
Module: 7-to_kv
Contains a function to_kv to create a tuple with the square of an int/float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with the square of an int/float value.

    Args:
        k (str): The string key.
        v (Union[int, float]): The int or float value.

    Returns:
        Tuple[str, float]: A tuple with the string key and the square
    """
    return (k, float(v ** 2))
