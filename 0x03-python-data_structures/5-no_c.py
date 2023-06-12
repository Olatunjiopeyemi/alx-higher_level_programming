#!/usr/bin/python3
def no_c(my_string):
    new = my_string.translate({ord(n): None for n in 'cC'})
    return new
