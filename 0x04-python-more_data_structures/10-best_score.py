#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    biggest = max(a_dictionary.values())
    for key, val in a_dictionary.items():
        if val == biggest:
            return key
