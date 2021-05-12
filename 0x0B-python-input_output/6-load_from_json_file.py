#!/usr/bin/python3
""" this function creates an object from a JSON file """


import json


def load_from_json_file(filename):
    """ creates an object from a JSON file """

    with open(filename) as f:
        return json.loads(f.read())
