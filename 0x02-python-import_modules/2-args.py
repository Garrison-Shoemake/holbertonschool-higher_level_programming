#!/usr/bin/python3
import sys
args = len(sys.argv)
if __name__ == "__main__":
    for i in range(0, args):
        if i == 0:
            print("0 arguments.")
        elif args > 0:
            if args == 1:
                print("1 argument:")
                print("{}: {}".format(i, sys.argv[i]))
            else:
                print("{} arguments:".format(args))
                print("{}: {}".format(i, sys.argv[i]))
