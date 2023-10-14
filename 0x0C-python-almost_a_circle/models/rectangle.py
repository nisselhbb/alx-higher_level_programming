#!/usr/bin/python3
from models.base import Base
"""defining a Rectangle class"""


class Rectangle(Base):
    """an inherited class representing a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        intializes a regtangle instance
        args: width, height, x, y
            width: the width of the rectangle
            height: the height of the rectangle
            x (int): x-coordinate of the rectangle
            y (int): y-coordinate of the rectangle
            id: the id of the rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """gets and returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
    sets the width of the rec
    args: value(int): the new width of the rec
    Raises:
        TypeError: if the value is not an integer
        ValueError: if the value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """gets and returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
    sets the height of the rec
    args: value(int): the new height of the rec
    Raises:
        TypeError: if the value is not an integer
        ValueError: if the value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """gets and returns the x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """
    sets the x coordinate of the rec
    args: value(int): the coordinate value of the rec
    Raises:
        TypeError: if the value is not an integer
        ValueError: if the value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """gets and returns the y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """
    sets the y coordinate of the rec
    args: value(int): the coordinate value of the rec
    Raises:
        TypeError: if the value is not an integer
        ValueError: if the value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area value of the Rectangle instance"""
        return self.__height * self.__width

    def display(self):
        """prints in stdout the Rectangle instance with the character
        #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rec_string = ""
        for i in range(self.__height):
            rec_string += "#" * self.__width
            if i < self.__height - 1:
                rec_string += "\n"
        print(rec_string)
