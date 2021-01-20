#!/usr/bin/python3
""" Module to create a function """


def read_file(filename=""):
    """ Function to read a file and print it in stdout """

    with open(filename) as f:
        for line in f:
            print(line, end="")
