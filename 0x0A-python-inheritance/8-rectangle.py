#!/usr/bin/python3
""" New Class named BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ Subclass of BaseGeometry """

    def __init__(self, width, height):
        if super().integer_validator("width", width):
            self.width = width
        if super().integer_validator("height", height):
            self.height = height
