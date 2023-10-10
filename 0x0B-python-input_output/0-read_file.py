#!/usr/bin/python3
"""defining a read_file function"""


def read_file(filename=""):
    """a function that readsa text file"""
    with open(filename, encoding="UTF-8") as f:
        read_data = f.read()
        print(read_data, end="")
