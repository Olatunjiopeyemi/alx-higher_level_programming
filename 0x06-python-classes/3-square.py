#!/usr/bin/python3


"""
A square class with a class module
"""


class Square:
"""
initializing 
args: size (int):
"""
    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size


    def area(self):
        """
        returns rhe current square area
        """
        return int(self.__size) * int(self.__size)
