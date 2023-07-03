#!/usr/bin/python3

"""A class that defines a rectangle based on 3-rectangle.py"""


class Rectangle:
    """Creating a class"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """creating a property instance"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value


     @property
    def height(self):
        """Get/set the current size of the rectangle."""
        return (self.__size)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
         """Return the current area of the rectangle"""
         return (self.__width) * (self.__height)
     def perimeter(self):
         """Returning the perimeter"""
         if (self.__width) == 0 or (self.__height) == 0:
             return 0
         return (self.__height * 2) * (self.__width * 2)


     def __str__(self):
        """Return the printable rep of rectangle with the # character.
        """

        if self.__width == 0 or self.__height == 0:
            return ("")

        string = []
        for n in range(self.__height):
            [string.append('#') for j in range(self.__width)]
            if n != self.__height - 1:
                string.append("\n")
        return ("".join(string))

     def __repr__(self):
         """Return a string rep of the rectangle to create an new instance"""
         return f"Rectangle({self.width}, {self.height})"
