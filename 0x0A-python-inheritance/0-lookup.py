#!/usr/bin/python3
"""Defines an object attribute lookup function"""


def lookup(obj) -> list:
    """
    Returns:
        list: A list of the objects attributes and methods.
    """
    return dir(obj)
