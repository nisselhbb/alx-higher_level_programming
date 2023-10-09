#!/usr/bin/python3
"""defining BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class that raises an Exception"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value
            Raises:
                TypeError: if value is not an integer
                ValueError: if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
