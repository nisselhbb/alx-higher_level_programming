#!/usr/bin/python3
"""defining a the 1st class Base"""
import csv


class Base:
    """this class is the base for all others classes"""
    __nb_objects = 0


    def __init__(self, id=None):
        """initialization
        args: id: an integer"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
