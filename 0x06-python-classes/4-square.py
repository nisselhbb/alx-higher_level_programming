#!/usr/bin/python3
"""defines a class"""


class Square:
    def __init__(self, size=0):
        """__size: the size of the square
    __init__(self, size): initializes a square instance
    Args:
    size"""
        self.__size = size

    @property
    def size(self):
        """getter method to retrieve the
        size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """computes and returns the size of the current
        square area"""
        return self.__size ** 2
