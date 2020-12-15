#!/usr/bin/python3
def no_c(my_string):
    string2 = ""
    for i in range(0, len(my_string)):
        if my_string[i] == "C" or my_string[i] == "c":
            pass
        else:
            string2 = string2 + my_string[i]
    return (string2)
