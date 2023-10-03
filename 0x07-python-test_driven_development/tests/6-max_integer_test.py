#!/usr/bin/python3
"""modle unittest for the max_integer function"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """testing when the input list is empty"""
        self.assertIsNone(max_integer([]),)

    def test_single_element_list(self):
        """testing when the input list has a single element"""
        self.assertEqual(max_integer([1]), 1)

    def test_positive_numbers(self):
        """testing when the input list has positive numbers"""
        self.assertEqual(max_integer([1, 20, 30, 40, 50]), 50)

    def test_negative_numbers(self):
        """testing when the input list has negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers(self):
        """testing when the iput list has both negative and positive numbers"""
        self.assertEqual(max_integer([-1, 3, 7, 2, -9]), 7)

    def test_duplicate_max(self):
        """testing when the input list has equal integers"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_ints_and_floats(self):
        """testing when the input list has integers and floats"""
        self.assertEqual(max_integer([1.50, 20.4, -7, 10]), 20.4)

    def test_empty_string(self):
        """testing when the input is an empty string"""
        self.assertEqual(max_integer(""), None)

    def test_list_of_strings(self):
        """testing when the input is list of strings"""
        self.assertEqual(max_integer(["My", "name", "is"]), "name")

     def test_non_int_arg(self):
        """testing when there is a non-int type in list"""
        string = [1, 2, "Hello", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(string)


if __name__ == '__main__':
    unittest.main()
