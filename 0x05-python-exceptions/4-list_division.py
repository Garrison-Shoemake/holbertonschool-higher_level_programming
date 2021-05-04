#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = list()
    tot = 0
    for i in range(list_length):
        try:
            tot = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            tot = 0
        except IndexError:
            print("out of range")
            tot = 0
        except ZeroDivisionError:
            print("division by 0")
            tot = 0
        finally:
            newlist.append(tot)
    return newlist
