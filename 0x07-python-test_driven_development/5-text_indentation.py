#!/usr/bin/python3
""" Function will print a text with two new lines after certain characters """


def text_indentation(text):
    """ this function checks for a string first then separates based
    on delimiters found """


    if not isinstance(text, str):
        raise TypeError("text must be a string")

    idx = 0
    for idx in text:
        if idx == ' ' and starting == 1:
            continue

        if idx == '.' or idx == '?' or idx == ':':
            print("{}{}".format(idx, '\n'))
            starting = 1
        else:
            print(idx, end="")
            starting = 0
