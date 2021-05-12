#!/usr/bin/python3
""" This function writes a string to a text file and returns character count """


def write_file(filename="", text=""):
    """ this function calls with and print with a counter variable
    return the counter variable, function should creat the file
    if it doesnt exist and overwrites the content if it exists """

    with open(filename, 'w') as f:
        return f.write(text)
