#!/usr/bin/python3
""" Square will now have a check on size"""


class Square():
    """ Square's only attribute is size atm """

    def __init__(self, size=0):
        """ Initialization method, variables go here
        In addition, this checks that size is 0 or more """

        tf = isinstance(size, int)
        if tf is True:
            self.__size = size
        else:
            print("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
