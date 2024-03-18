#!/usr/bin/env python3
"""duck-typed annotations - first element of a sequence
"""


from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return first element of lst if there is any, otherwise None."""
    if lst:
        return lst[0]
    else:
        return None
