#!/usr/bin/python3
def islower(c):
    for i in range(0, len(c)):
        if ord(chr(i)) >= 97 and ord(chr(i)) <= 122:
            return True
        else:
            return False
