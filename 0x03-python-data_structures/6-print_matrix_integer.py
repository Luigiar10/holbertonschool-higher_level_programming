#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for x in i[:-1]:
            print("{:d}".format(x), end=" ")
        if i:
            print("{:d}".format(i[-1]))
