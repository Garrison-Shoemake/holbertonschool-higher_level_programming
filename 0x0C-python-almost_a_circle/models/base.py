#!/usr/bin/python3
""" This is our Base Class file """


import json


class Base:
    """ Base Class information goes here """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        newlist = []
        filename = cls.__name__ + '.json'
        if list_objs is not None:
            for i in list_objs:
                newlist.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(newlist))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == []:
            return "[]"
        else:
            return json.dumps(json_string)
