#!/usr/bin/python3
"""defining a class nthat inherits from another
class"""


class MyList(list):
    """the MyList class that inherits from list
        prints the list, but sorted in an asceding order"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
