#!/usr/bin/env python3

"""
Module: 8-make_multiplier
Contains a function make_multiplier to create a function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier to be used.

    Returns:
        Callable[[float], float]: A function that multiplies
    """
    def multiplier_function(num: float) -> float:
        """
        Multiplies a float by the given multiplier.

        Args:
            num (float): The float to be multiplied.

        Returns:
            float: The result of the multiplication.
        """
        return num * multiplier

    return multiplier_function
