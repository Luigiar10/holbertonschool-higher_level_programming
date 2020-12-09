#!/usr/bin/python3
for x in range(10):
    for i in range(10):
        if i > x:
            print('{}'.format(x), end='')
            if x != 8 or i != 9:
                print('{}'.format(i), end=', ')
            else:
                print('{}'.format(i))
