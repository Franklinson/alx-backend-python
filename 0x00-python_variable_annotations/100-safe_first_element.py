#!/usr/bin/env python3
"""use more duck-type annotations in function declarations"""


import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
        typing.Union[typing.Any, None]:
    """Duck-typed annotation"""
    if lst:
        return lst[0]
    else:
        return None
