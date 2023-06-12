#!/usr/bin/python3

def multiple_returns(sentence):
    N = ()
    if len(sentence) == 0:
        N = 0, None
    else:
        N = len(sentence), sentence[0]
    return N
