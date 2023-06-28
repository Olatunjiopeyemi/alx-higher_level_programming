#!/usr/bin/python3

class Square:

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value is not tuple) or
            any(type(n)is not int for n in value) or 
            len(value) != 2 or
            any(n < 0 for n in value):
        raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return int(self.__size) * int(self.__size)

    def my_print(self):
        if self.__size > 0:
            for n in range (self.__size):
                print("#" * self.__size)
        else if self.__size == 0:
            print("")

