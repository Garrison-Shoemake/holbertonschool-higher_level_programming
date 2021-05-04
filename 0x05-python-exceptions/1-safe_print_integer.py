#!/usr/bin/python3
def safe_print_integer(value):
    tf = isinstance(value, int)
    try:
        print("{:d}".format(value))
        return tf

    except:
        return tf
