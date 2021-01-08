#!/usr/bin/python3
""" Function to print a square """


def print_square(size):
    """
    Function to print a square and raise some errors
    for edge cases
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for y in range(size):
        print("#" * size)
