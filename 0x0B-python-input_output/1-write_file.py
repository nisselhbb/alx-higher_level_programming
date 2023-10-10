#!/usr/bin/python3
"""defining a write_file function"""


def write_file(filename="", text=""):
    """writes a string to the text file, and returns the number
        of characters written"""
    with open(filename, "w", encoding="UTF-8") as f:
        characters = f.write(text)
        return characters
