#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
# doubling every item in a 2d matrix

    newmatrix = []
    for col in matrix:
        res = (list(map((lambda x: x**2, n))))
        newmatrix.append(res)
    return newmatrix
