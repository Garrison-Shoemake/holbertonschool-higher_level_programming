#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(chr(i)) >= 97 and ord(chr(i)) <= 122:
            print("{}".format(chr(i - 32)))
        else:
            print("{}".format(chr(i)))
