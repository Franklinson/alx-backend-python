#!/usr/bin/env python3
""" type annotation takes list of float and returns sum """


from typing import List


def sum_list(input_list: List[float]) -> float:
    '''returns the sum of a float '''
    return float(sum(input_list))
