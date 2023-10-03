#!/usr/bin/python3
"""a funtion that prints a square with
    the character #"""


def print_square(size):
    """
    prints a square with teh character #
    args:
        size: thz size of the square
    raises:
        TypeError: if size is not an integer/ if it is
            a float and is less than 0
        ValueError: if size if less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print(("#" * size + '\n') * size, end="")
