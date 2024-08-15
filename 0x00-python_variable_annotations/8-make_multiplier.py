#!/usr/bin/env python3
"""
type-annotated function that takes a float and
returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_fun(x: float) -> float:
        """
        function that takes a float and returns a function
        that multiplies a float by multiplier
        """
        return x * multiplier

    return multiplier_fun
