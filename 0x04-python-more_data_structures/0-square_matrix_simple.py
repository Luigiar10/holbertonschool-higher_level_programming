#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = []
    for row in matrix:
        matrix2.append([item ** 2 for item in row])
    return matrix2
    return matrix