#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    else:
        my_list.reverse()
        for element in my_list:
            print("{}".format(element))
