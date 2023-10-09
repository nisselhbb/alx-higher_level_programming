#!/usr/bin/python3
"""defining a subclass Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """the subclass Square"""
    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """the Square area"""
        return self.__size ** 2
