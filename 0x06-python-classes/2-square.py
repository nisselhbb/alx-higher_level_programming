#!/usr/bin/python3
"""defines a class square"""


class Square:
    """represents a class square"""
    def __init__(self, size=0):
        """size: the size of the square
        __init__(self, size=0): initializes a square instance
        Args:
        size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        """Exceptionn raised:
            TypeError: if the size is not an integer
            ValueError: if the size value is less than 0"""
        self.__size = size
