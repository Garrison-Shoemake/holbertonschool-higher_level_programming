#!/usr/bin/python3
""" This is a basic addition function """

def add_integer(a, b=98):
""" Checks both a and b for correct type and converts if needed """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
