#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    maxi = list[0]
    n = 1
    while n < len(list):
        if list[n] > maxi:
            maxi = list[n]
        n += 1
    return maxi
