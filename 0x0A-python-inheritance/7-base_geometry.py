#!/usr/bin/python3
"""defines class BseGeometry"""


class BaseGeometry:
    """BaseGeometry class athat raises an Exception"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that the value is an integer"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
