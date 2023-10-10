#!/usr/bin/python3
"""defining an append_write function"""


def append_write(filename="", text=""):
    """appends a string at the end of the text file"""
    with open(filename, "a", encoding="UTF-8") as f:
        characters_added = f.write(text)
        return characters_added
