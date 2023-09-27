#!/usr/bin/python3
"""defines a class square"""


class Square:
    """represents a class square"""
    def __init__(self, size=0, position=(0, 0)):
        """__size: the size of the square
    __init__(self, size): initializes a square instance
    Args:
    size"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """getter mothod to retrieve the position
        of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """computes and returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print('#' * self.__size)
