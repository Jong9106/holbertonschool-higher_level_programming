#!/usr/bin/python3
""" Module to create a function """


def append_write(filename="", text=""):
    """ Function to append a text in a file """

    with open(filename, 'a') as f:
            return f.write(text)
