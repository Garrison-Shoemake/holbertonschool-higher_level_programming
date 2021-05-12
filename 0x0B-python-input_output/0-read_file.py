#!/usr/bin/python3
""" This function reads a text file and prints it to stdout """


def read_file(filename=""):
    """ Here we open the file with with and print """

    with open(filename) as f:
        print(f.read(), end="")
