#!/usr/bin/python3
"""defining an add_item function that adds all arguments to a Python list,
    and then save them to a file"""
import sys
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    py_list = load_from_json_file(filename)
except FileNotFoundError:
    py_list = []
for arg in sys.argv:
    if arg == sys.argv[0]:
        continue
    py_list.append(arg)
    save_to_json_file(py_list, filename)
