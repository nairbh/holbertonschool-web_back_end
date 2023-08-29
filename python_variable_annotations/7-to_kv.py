#!/usr/bin/env python3
"""string"""
from typing import Union, Tuple


def to_kv(a: str, b: Union[int, float]) -> Tuple[str, float]:
    """ function """
    square = (b * b)
    result: Tuple[str, float] = (a, square)
    return result
