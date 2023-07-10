#!/usr/bin/python3
""" a Rectangle subclass Square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size: int):
         super().integer_validator("size", size)
        self.__size = size

    def area(self) -> int:
        """Computes the area of the rectangle.

        Returns:
            int: The area.
        """
        return self.__size * self.__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
