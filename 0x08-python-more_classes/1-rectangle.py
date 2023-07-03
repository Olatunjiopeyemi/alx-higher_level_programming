#!/usr/bin/python3

"""Defining a rectangle based on 0-rectangle.py"""


class Rectangle:
    """class defined"""

    def __init__(self, width=0, height=0):
         """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.height = height
        self.width = width


    @property
    def height(self):
        """Creating a property instsnce"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """initializing height setter"""
        if type(value) is not int:
            raise typeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """creating  a property"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """initializing a setter for the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

