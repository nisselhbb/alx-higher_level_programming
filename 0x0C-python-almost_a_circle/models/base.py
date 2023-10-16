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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, encoding="UTF-8") as f:
                inst = f.read()
                if not inst:
                    return []
                list_dicts = cls.from_json_string(inst)
                return [cls.create(**di) for di in list_dicts]
        except FileNotFoundError:
            return []
