#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for coln in row:
            print("{:d}".format(coln), end=" " if coln != row[-1] else "")
        print()
