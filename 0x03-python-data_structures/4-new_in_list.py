#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    else:
        listnew = my_list[:]
        listnew[idx] = element
        return (listnew)
