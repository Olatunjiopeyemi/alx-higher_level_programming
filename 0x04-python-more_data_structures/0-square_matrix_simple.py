#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    newmatrix = []
    for row in matrix:
        res = (list(filter((lambda x: x**2, row))))
        newmatrix.append(result)
    return newmatrix
