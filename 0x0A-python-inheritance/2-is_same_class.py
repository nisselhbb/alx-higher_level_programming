#!/usr/bin/python3
"""defining is_same_class function"""


def is_same_class(obj, a_class):
    """ a function that returns
        True: if the object is exactly an instance
        False: othewise"""
    return type(obj) is a_class
