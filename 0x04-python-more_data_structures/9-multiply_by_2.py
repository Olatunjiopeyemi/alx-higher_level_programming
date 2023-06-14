#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    newdic = {}
    for keys, value in a_dictionary.items():
        newdic.update({keys: (value*2)})
    return newdic
