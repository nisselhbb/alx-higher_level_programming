#!/usr/bin/python3
"""defining a the 1st class Base"""
import csv
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """"writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        list_dict = []
        if list_objs:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())
        with open(filename, "w", encoding="UTF-8") as f:
            f.write(cls.to_json_string(list_dict))
