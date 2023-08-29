#!/usr/bin/env python3
"""mixed list"""
from typing import List
from typing import Union


def sum_mixed_list(list: List[Union[int, float]]) -> float:
    """ Write annotated function mixed list"""
    result: float = 0
    for i in list:
        result += i
    return result
