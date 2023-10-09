#!/usr/bin/python3
"""defining a function"""


def add_attribute(obj, attr, value):
    """adds a new attribute to an object if possible"""
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
