#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string:
        numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i, c in enumerate(roman_string):
            if (i + 1) ==
            len(roman_string) or numbers[c] >= numbers[roman_string[i + 1]]:
                result += numbers[c]
            else:
                result -= numbers[c]
        return result
    return 0
