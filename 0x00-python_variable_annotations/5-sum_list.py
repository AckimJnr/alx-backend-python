#!/usr/bin/env python3
"""
list annotation
"""
from typing import List


def sum_list(input_list: List[float] = []) -> float:
    """
    Return sum of a list as float
    input_list: list to process
    """
    list_sum: float = 0

    for x in input_list:
        list_sum += x

    return list_sum
