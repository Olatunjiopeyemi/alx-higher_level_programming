#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    newmatrix = []
    for col in matrix:
        res = (list(filter((lambda x: x**2, col))))
        newmatrix.append(res)
    return newmatrix
