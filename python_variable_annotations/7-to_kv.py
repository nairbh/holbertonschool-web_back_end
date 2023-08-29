#!/usr/bin/env python3
"""string"""
from typing import Union, Tuple


def to_kv(v: str, k: Union[int, float]) -> Tuple[str, float]:
    """ function """
    square = (v * v)
    result: Tuple[str, float] = (k, square)
    return result
