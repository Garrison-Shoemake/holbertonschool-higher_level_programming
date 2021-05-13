#!/usr/bin/python3
""" this file includes a class with definitions """


class Student():
    """ This class covers students, with parameters: first
    and last name and age. """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        atts = {}

        if attrs != None:
            for i in attrs:
                if i in self.__dict__:
                    atts[i] = self.__dict__[i]
            return atts
        else:
            return vars(self)
