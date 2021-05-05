#!/usr/bin/python3
""" Square will now have a check on size"""


class Square():
    """ Square's only attribute is size atm """

    def __init__(self, size=0):
        """ Initialization method, variables go here
        In addition, this checks that size is 0 or more """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size**2)
