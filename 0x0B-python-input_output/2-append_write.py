#!/usr/bin/python3
""" This function appends a string to a file! """


def append_write(filename="", text=""):
    """ apppends to the end of a file then returns character count """

    with open(filename, 'a') as f:
        return f.write(text)
