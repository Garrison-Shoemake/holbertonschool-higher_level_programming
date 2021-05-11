#!/usr/bin/python3
""" This Class will inherit from list """


class MyList(list):
    """ MyList will print a list, sorted in ascending order """

    def print_sorted(self):
        print(sorted(self))
