#!/usr/bin/python3

def uniq_add(my_list=[]):
    myset = []
    sum = 0
    for n in my_list:
        if n not in myset:
            myset.append(n)
            sum += n
    return sum
