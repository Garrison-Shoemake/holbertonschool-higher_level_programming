#!/usr/bin/python3
""" this function checks an instance for its class """


def is_same_class(obj, a_class):
    """ runs isinstance """

    if isinstance(obj, a_class) and type(obj) == a_class:
        return True
    else:
        return False
