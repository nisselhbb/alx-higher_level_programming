#!/usr/bin/python3
"""defining a rectangle"""


class Rectangle:
    """a class representing a rectangle"""
    def __init__(self, width=0, height=0):
        """
        initializes a rectangle instance
        Attribute:
            width: the width of the rec
            height: the height of the rec
        args: width, height
            """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ gets and returns the width of the rec"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width of the rec
        args: value(int): ther new width of the rec
        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than 0
            """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets and returns the height of the rec"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height of the rec
        args: value(int): the new height of teh rec
        Raises:
            TypeError: if the value is not an integer
            ValueErroe: if the value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
