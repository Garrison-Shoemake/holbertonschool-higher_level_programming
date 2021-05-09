#!/usr/bin/python3
""" This function prints a name! """


def say_my_name(first_name, last_name=""):
    """ This is the function that prints a name,
    after checking that it is a string """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
