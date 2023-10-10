#!/usr/bin/python3
"""defining a from_json_string function"""
import json


def from_json_string(my_str):
    """return an object (Python data structure) represented by
        JSON string"""
    return json.loads(my_str)
