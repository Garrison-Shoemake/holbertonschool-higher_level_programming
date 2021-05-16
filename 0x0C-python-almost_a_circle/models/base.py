#!/usr/bin/python3
""" This is our Base Class file """

class Base:
    """ Base Class information goes here """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
