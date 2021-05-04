#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for x in my_list:
                print("{}".format(my_list[x]), end="")
    except:
        pass
    print()
    return x
