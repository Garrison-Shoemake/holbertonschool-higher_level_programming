#!/usr/bin/python3
""" New Class named BaseGeometry """


class BaseGeometry:
    """ BaseGeometry, class that raises and exception for area and
    validates a value given in integer_validator """

    def area(self):
        """ currently empty, only raises exception """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance (value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ Subclass of BaseGeometry """

    def __init__(self, width, height):
        super().__init__()
        if super().integer_validator("width", width):
            self.width = width
        if super().integer_validator("height", height):
            self.height = height
