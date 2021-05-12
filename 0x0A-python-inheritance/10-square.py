#!/usr/bin/python3
""" imports task 9 and creates new subclass """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ this is a square class, subclass of rectangle, subclass of
    BaseGeometry class """

    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
