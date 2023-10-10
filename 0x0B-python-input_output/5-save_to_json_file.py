#!/usr/bin/python3
"""defining a save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using JSON representation"""
    with open(filename, "w", encoding="UTF-8") as f:
        return json.dump(my_obj, f)
