#!/usr/bin/python3

class Square:

    def __init__(self, size=0):

        self.__size = size

    @property
    def size(self):

        return self.__size

    @size.setter
    def size(self, value):
        if no isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        return int(self.__size) * int(self.__size)

    def my_print(self):
        if self.__size > 0:

            for n in range(self.__size):
                print("#" * self.__size)

        elif self.__size == 0:
            print("")
            
