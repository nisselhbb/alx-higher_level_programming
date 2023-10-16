import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertIsNotNone(rect.id)

    def test_width_property(self):
        rect = Rectangle(5, 10)
        rect.width = 15
        self.assertEqual(rect.width, 15)

    def test_height_property(self):
        rect = Rectangle(5, 10)
        rect.height = 20
        self.assertEqual(rect.height, 20)

    def test_x_property(self):
        rect = Rectangle(5, 10)
        rect.x = 3
        self.assertEqual(rect.x, 3)

    def test_y_property(self):
        rect = Rectangle(5, 10)
        rect.y = 2
        self.assertEqual(rect.y, 2)

    def test_area(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_display(self):
        rect = Rectangle(3, 2, 1, 1)
        with self.assertLogs() as logs:
            rect.display()
            self.assertEqual(logs.output, ['   #', '   #'])

    def test_str(self):
        rect = Rectangle(5, 10, 2, 3, 42)
        self.assertEqual(str(rect), "[Rectangle] (42) 2/3 - 5/10")

    def test_update(self):
        rect = Rectangle(5, 10)
        rect.update(1, 15, 20, 3, 2)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 2)

    def test_to_dictionary(self):
        rect = Rectangle(5, 10, 2, 3, 42)
        rect_dict = rect.to_dictionary()
        expected_dict = {'x': 2, 'y': 3, 'id': 42, 'width': 5, 'height': 10}
        self.assertEqual(rect_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
