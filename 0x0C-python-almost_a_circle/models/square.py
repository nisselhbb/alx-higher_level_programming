#!/usr/bin/python3
"""importing rectangle"""
from models.rectangle import Rectangle
"""defining a Square class"""


class Square(Rectangle):
    """an inherited class representing a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        initializes a square instance
        size: the size of the square
        x: x-coordinate of the square
        y: y-coordinate of the square
        id: the id of the square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns [Square] (<id>) <x>/<y> - <size>, where in
        this case size is whether the width or the height"""
        one = str(f"{self.x}/{self.y}")
        return f"[Square] ({self.id}) {one} - {self.width}"

    @property
    def size(self):
        """gets an returns the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the value of the square"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns arguments to attributes using *args
        and **kwargs"""
        if args:
            attr = ["id", "size", "x", "y"]
            for j, arg in enumerate(args):
                setattr(self, attr[j], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {'id': self.id, 'x': self.x,
                'size': self.size, 'y': self.y}
