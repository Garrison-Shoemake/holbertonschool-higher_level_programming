#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ii = 0
    for i in range(x):
        try:
            tf = isinstance(my_list[i], int)
            if tf == True:
                print("{}".format(my_list[i]), end="")
                ii += 1
        except:
            return
    print()
    return ii
