#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string == None:
        return 0

    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if any(ch not in numerals for ch in roman_string):
        return 0

    roman_num = numerals[roman_string[0]]
    for n, x in enumerate(roman_string[1:], 1):
        if numerals[roman_string[n-1]] < numerals[roman_string[n]]:
           roman_num += numerals[roman_string[n]] - 2*(numerals[roman_string[n-1]])
        else:
            roman_num += numerals[x]

    return roman_num
