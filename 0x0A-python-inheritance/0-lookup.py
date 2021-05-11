#!/usr/bin/python3
""" This function will return a list of attributes and methods of an object """


def lookup(obj):
    """ This function returns list of attribuest of obj """

    lst = []
    lst = dir(obj)
    return lst
