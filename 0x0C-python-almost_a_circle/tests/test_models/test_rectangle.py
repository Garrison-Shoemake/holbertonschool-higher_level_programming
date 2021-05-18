#!/usr/bin/python3
""" this is the unittest file for the Base class """


import unittest
from models.rectangle import Rectangle


class RectTest(unittest.TestCase):
    """ These are the unit tests for the base class """

    def test_basics(self):
        r = Rectangle(3, 4, 5, 6)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    def test_negatives(self):
        """ this method tests for negative numbers in Rectangle """

        with self.assertRaises(ValueError):
            b1 = Rectangle(-1, 2, 3, 4)
        with self.assertRaises(ValueError):
            b2 = Rectangle(1, -2, 3, 4)
        with self.assertRaises(ValueError):
            b3 = Rectangle(1, 2, -3, 4)
        with self.assertRaises(ValueError):
            b4 = Rectangle(1, 2, 3, -4)

    def test_strings(self):
        """ this method tests for strings in Rectangle """

        with self.assertRaises(TypeError):
            b1 = Rectangle("1", 2, 3, 4)
        with self.assertRaises(TypeError):
            b2 = Rectangle(1, "2", 3, 4)
        with self.assertRaises(TypeError):
            b3 = Rectangle(1, 2, "3", 4)
        with self.assertRaises(TypeError):
            b4 = Rectangle(1, 2, 3, "4")

    def test_zero(self):
        """ this method tests if width and height are 0 """

        with self.assertRaises(ValueError):
            b1 = Rectangle(0, 1)

        with self.assertRaises(ValueError):
            b2 = Rectangle(2, 0)

    def test_update(self):
        r = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/1")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/1")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/0 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

if __name__ == '__main__':
    unittest.main()
