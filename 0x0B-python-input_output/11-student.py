#!/usr/bin/python3
"""defining a Student class"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
            Args:
                attrs:a list of attribute names to be
                included in the dictionary. If provided, only the
                specified attributes are included; otherwise,
                all attributes are included
        """
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for key in attrs:
                if key in self.__dict__:
                    result[key] = self.__dict__[key]
            return result

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        return self.__dict__.update(json)
