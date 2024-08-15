#!/usr/bin/env python3
"""
type annotated function that takes a list od floats
and returns their sum as float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    function that takes a list od floats
    and returns their sum as float
    """
    return sum(input_list)
