#!/usr/bin/python3
"""defines a class square"""


class Square:
    """represents a class square"""
    def __init__(self, size=0):
        """__size: the size of the square
    __init__(self, size): initializes a square instance
    Args:
    size"""
        self.__size = size

    @property
    def size(self):
        """getter method to retrive
        the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets value of the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """computes and returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print('#' * self.__size)
