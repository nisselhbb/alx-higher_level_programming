#!/usr/bin/python3
"""writing a function that adds 2 integers"""


def add_integer(a, b=98):
    """
    adds two integers
    args:
        a: the 1st number to be added
        b: the 2nd number to be added
    raises:
        TypeError: if both a and b are not integers or
            floats
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
