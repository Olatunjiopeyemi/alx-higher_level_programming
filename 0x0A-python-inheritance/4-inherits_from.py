#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """
        Checks if an object is an instance of a subclass o a class
        but not exactly an instance of a class itself.

    Args:
        obj (any): Any data type
        a_class (type): Any class object

    Returns:
        bool: True or False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
