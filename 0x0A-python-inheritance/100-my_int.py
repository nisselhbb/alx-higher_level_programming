#!/usr/bin/python3
"""defining Myint class"""


class MyInt(int):
    """MyInt subclass"""
    def __eq__(self, other):
        """inverts == to use !="""
        return super().__ne__(other)

    def __ne__(self, other):
        """inverts != to use =="""
        return super().__eq__(other)
