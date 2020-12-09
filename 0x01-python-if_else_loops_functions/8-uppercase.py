#!/usr/bin/python3
def uppercase(str):
    for j in str:
        if ord(j) < 123 and ord(j) > 96:
            j = chr(ord(j) - 32)
        print('{:}'.format(j), end='')
    print('')