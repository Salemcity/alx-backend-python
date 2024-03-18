#!/usr/bin/env python3
"""Basic annotations - to the below function"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return list of tuples, one for each item in lst,
    of the item and its length."""
    return [(i, len(i)) for i in lst]
