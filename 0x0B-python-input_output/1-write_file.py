#!/usr/bin/python3
""" Module to create a function """


def write_file(filename="", text=""):
    """ Function to write a text into a file """

    with open(filename, 'w') as f:
        return f.write(text)
