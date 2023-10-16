#!/usr/bin/python3
"""unit testing for square"""


import io
import sys
from models.base import Base
from models.square import Square
import unittest


class TestSquare(unittest.TestCase):
    def test_init(self):
        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertIsNotNone(square.id)

    def test_size_property(self):
        square = Square(5)
        square.size = 10
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

    def test_str(self):
        square = Square(5, 2, 3, 42)
        self.assertEqual(str(square), "[Square] (42) 2/3 - 5")

    def test_update(self):
        square = Square(5)
        square.update(1, 10, 3, 2)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 2)

    def test_to_dictionary(self):
        square = Square(5, 2, 3, 42)
        square_dict = square.to_dictionary()
        expected_dict = {'id': 42, 'x': 2, 'size': 5, 'y': 3}
        self.assertEqual(square_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
