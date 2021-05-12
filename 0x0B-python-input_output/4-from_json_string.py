#!/usr/bin/python3
""" this function will return an object from a JSON string """


import json


def from_json_string(my_str):
    """ decodes a JSON file """

    return json.loads(my_str)
