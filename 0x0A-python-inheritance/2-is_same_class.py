#!/usr/bin/python3
"""A Class Function"""


def is_same_class(obj, a_class) -> bool:
    """Checks if `obj` is an exact instance of a given `class`.

    Args:
        obj (any): Any data type
        a_class (type): A class object to match

    Returns:
        bool: True or False
    """
    return type(obj) is a_class
