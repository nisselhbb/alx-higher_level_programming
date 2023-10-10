#!/usr/bin/python3
"""defining an append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file, after each line
        containing a specific string"""
    with open(filename, "r", encoding="UTF-8") as f:
        lines = f.readlines()
        specific_string = []

        for line in lines:
            specific_string.append(line)
            if search_string in line:
                specific_string.append(new_string + '\n')

    with open(filename, "w", encoding="UTF-8") as f:
        f.writelines(specific_string)
