#!/usr/bin/python3
"""writing a function that prints 1st
    and last name"""


def say_my_name(first_name, last_name=""):
    """
    prints full name
    args:
        first_name: 1st name
        last_name: the last name
    raises:
        TypeError: if the 1st or the last name are not
        strings
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
