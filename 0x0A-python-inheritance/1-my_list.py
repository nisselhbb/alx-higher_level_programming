#!/usr/bin/python3
"""defining a mylist class"""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
        """prints the list, but sorted in asceding order"""
        sorted_list = sorted(self)
        print(sorted_list)
