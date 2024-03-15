#!/usr/bin/env python3

"""
Module: 6-sum_mixed_list
Contains a function sum_mixed_list to compute the sum of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Compute the sum of integers and floats in a list.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
        float: The sum of the elements in the list.
    """
    return float(sum(mxd_lst))
