#!/usr/bin/python3
"""defining a rectangle"""


class Rectangle:
    """a class representing a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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

    def area(self):
        """calculates and returns the area of the rec"""
        return self.width * self.height

    def perimeter(self):
        """calculates and returns the perimeter of the rec"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """
        returns a string representation of the rec
        rec_string: a string representing the rec
        """
        if self.width == 0 or self.height == 0:
            return ""
        rec_string = ""
        for i in range(self.height):
            rec_string += str(self.print_symbol) * self.width
            if i < self.height - 1:
                rec_string += "\n"
        return rec_string

    def __repr__(self):
        """returns a string representation of the object"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
