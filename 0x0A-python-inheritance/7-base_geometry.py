#!/usr/bin/python3
"""defining BaseGeomatry class"""


class BaseGeometry:
    """BaseGeotmetry class"""
    pass

    def area(self):
        """raising an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """value validation"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
