#!/usr/bin/python3
"""defining is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """
    a function that returns
        True: if tthe object is an instance of, or if the object
            is an instance of a class that inherited it
        False: otherwise
    """
    return isinstance(obj, a_class)
