#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    _score = 0
    _weight = 0

    for tup in my_list:
        _score += tup[0] * tup[1]
        _weight += tup[1]

    return (_score / weight)
