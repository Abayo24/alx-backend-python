#!/usr/bin/env python3
"""Augmented code with the correct duck-typed annotations"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Function that returns a safe element"""
    if lst:
        return lst[0]
    else:
        return None
