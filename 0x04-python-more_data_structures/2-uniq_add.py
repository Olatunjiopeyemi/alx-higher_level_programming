#!/usr/bin/python3

def uniq_add(my_list=[]):
    myset = set(my_list)
    sum = 0
    for n in myset:
        sum += n
        return sum
