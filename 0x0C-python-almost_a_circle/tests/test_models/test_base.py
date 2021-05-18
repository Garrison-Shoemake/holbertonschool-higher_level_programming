#!/usr/bin/python3
""" this is the unittest file for the Base class """


import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    """ These are the unit tests for the base class """

    def test_ids(self):
        """ docstring """

        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(None)
        self.assertEqual(b2.id, 2)

    def test_this(self):
        """ docstring """

        b1 = Base(15)
        self.assertEqual(b1.id, 15)
        self.assertRaises(TypeError)
        b2 = Base()

    if __name__ == '__main__':
        unittest.main()
