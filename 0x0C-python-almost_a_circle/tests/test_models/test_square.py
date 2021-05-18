#!/usr/bin/python3
""" this is the unittest file for the Base class """


import unittest
from models.square import Square


class SqrTest(unittest.TestCase):
    """ These are the unit tests for the base class """

    def test_basics2(self):
        s = Square(1)
        self.assertEqual(s.width, 1)
        s = Square(1, 2)
        self.assertEqual(s.x, 2)

    def test_basics(self):
        s = Square(3, 3, 5)
        self.assertEqual(s.width, 3)
        self.assertEqual(s.height, 3)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 5)

    def test_negatives(self):
        """ this method tests for negative numbers in Rectangle """

        with self.assertRaises(ValueError):
            b1 = Square(-1, 2, 3)
        with self.assertRaises(ValueError):
            b2 = Square(1, -2, 3)
        with self.assertRaises(ValueError):
            b3 = Square(1, 2, -3)

    def test_strings(self):
        """ this method tests for strings in Rectangle """

        with self.assertRaises(TypeError):
            b1 = Square("1", 2, 3)
        with self.assertRaises(TypeError):
            b2 = Square(1, "2", 3)
        with self.assertRaises(TypeError):
            b3 = Square(1, 2, "3")

    def test_zero(self):
        """ this method tests if width and height are 0 """

        with self.assertRaises(ValueError):
            b2 = Square(0, 2)

    def test_update(self):
        s = Square(1, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")
        s.update(1, 2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 2")
        s.update(1, 2, 3)
        self.assertEqual(str(s), "[Square] (1) 3/0 - 2")
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_area(self):
        s = Square(5, 5)
        self.assertEqual(s.area(), 25)

if __name__ == '__main__':
    unittest.main()
