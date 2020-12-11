#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    initial = 0
    for i in argv[1:]:
        initial += int(i)
    print(initial)
