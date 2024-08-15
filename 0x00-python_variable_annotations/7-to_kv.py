#!/usr/bin/env python3
"""
Type annotated function that takes a string
and an int or float and returns a tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    function that takes a string
    and an int or float and returns a tuple
    """
    return (k, float(v ** 2))
