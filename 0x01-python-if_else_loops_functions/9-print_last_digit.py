#!/usr/bin/python3
def print_last_digit(number):
    ld = number % 10
    if number < 0:
        ld = number % -10
        ld = -(ld)
    print(ld, end="")
    return (ld)
