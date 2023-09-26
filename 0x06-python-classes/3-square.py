#!/usr/bin/python3
"""defines a class square"""


class Square:
    """represents a class square"""
    def __init__(self, size=0):
        """__size: the size of the square
        __init__(self, size): initializes a square instance
        Args:
            size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """defines a the method area within the class
        Square
        It computes and returns the current square area"""
        return self.__size ** 2
