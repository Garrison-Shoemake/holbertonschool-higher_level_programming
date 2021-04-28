#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            var = chr(ord(str[i]) - 32)
        else:
            var = str[i]

        print("{}".format(var), end="")
    print("")
