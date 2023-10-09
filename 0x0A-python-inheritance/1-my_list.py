#!/usr/bin/python3
"""defining a mylist class"""


class MyList(list):
    """MyList class that prints the list, but sorted
        in asceding order"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
