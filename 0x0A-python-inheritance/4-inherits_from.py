#!/usr/bin/python3
""" this function runs issubclass """


def inherits_from(obj, a_class):
    """ returns issubclass """

    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
