#!/usr/bin/env python3
"""Annotating function's parameters to return appropriate types"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function that returns length of elements in a list"""
    return [(i, len(i)) for i in lst]
