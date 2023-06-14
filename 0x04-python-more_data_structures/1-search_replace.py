#!/usr/bin/python3

def search_replace(my_list, search, replace):
    newlist = []
    for n in my_list:
        if n == search:
            newlist.append(replace)
        else:
            newlist.append(n)
    return newlist
