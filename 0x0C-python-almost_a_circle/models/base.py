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
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ is "Square":
            dummy = cls(2)
        if cls.__name__ is "Rectangle":
            dummy = cls(2, 2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + '.json'
        new = []
        try:
            with open(filename, 'r') as f:
                new = cls.from_json_string(f.read())
                for i, j in enumerate(new):
                    new[i] = cls.create(**new[i])
            return new
        except:
            return []
