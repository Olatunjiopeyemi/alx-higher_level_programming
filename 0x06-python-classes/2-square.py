#!/usr/bin/python3

""" creating a class"""


class Square:
    """ representing a new square"""
    def __init__(self, size=0):
        """
        initializing
        arguments: size(int)
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

