#!/usr/bin/python3
""" This function will print a square equal to the size given """


def print_square(size):
    """ This function will raise errors if an integer is not given
    as well as if the value is equal or less than zero. """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
