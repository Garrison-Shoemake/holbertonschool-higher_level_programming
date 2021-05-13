#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_these(self):
        self.assertEqual(max_integer([1,2,3,4,5]), 5)
        self.assertRaises(TypeError, max_integer((1,2)))
        self.assertRaises(TypeError, max_integer([0.123, 3.14159]))
        self.assertRaises(TypeError, max_integer("string"))
