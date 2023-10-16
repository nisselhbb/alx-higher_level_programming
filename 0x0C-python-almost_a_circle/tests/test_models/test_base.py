import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_init(self):
        obj1 = Base()
        self.assertEqual(obj1.id, 1)

        obj2 = Base(5)
        self.assertEqual(obj2.id, 5)

    def test_to_json_string(self):
        data = [{"key1": "value1", "key2": "value2"}]
        json_string = Base.to_json_string(data)
        self.assertEqual(json_string, '[{"key1": "value1", "key2": "value2"}]')

    def test_save_to_file(self):
        obj1 = Base(1)
        obj2 = Base(2)
        Base.save_to_file([obj1, obj2])

        loaded_objects = Base.load_from_file()
        self.assertEqual(len(loaded_objects), 2)
        self.assertEqual(loaded_objects[0].id, 1)
        self.assertEqual(loaded_objects[1].id, 2)

    def test_from_json_string(self):
        json_string = '[{"key1": "value1", "key2": "value2"}]'
        data = Base.from_json_string(json_string)
        self.assertEqual(data, [{"key1": "value1", "key2": "value2"}])

    def test_create(self):
        dictionary = {"id": 1, "width": 10, "height": 20}
        obj = Base.create(**dictionary)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 10)
        self.assertEqual(obj.height, 20)

    def test_load_from_file(self):
        with open("Base.json", "w") as f:
            f.write('[{"id": 1, "width": 10, "height": 20},
                    {"id": 2, "width": 5, "height": 15}]')

        loaded_objects = Base.load_from_file()
        self.assertEqual(len(loaded_objects), 2)
        self.assertEqual(loaded_objects[0].id, 1)
        self.assertEqual(loaded_objects[0].width, 10)
        self.assertEqual(loaded_objects[0].height, 20)


if __name__ == '__main__':
    unittest.main()
