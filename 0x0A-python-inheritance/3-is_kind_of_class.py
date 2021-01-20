#!/usr/bin/python3
""" Function to check an instance of a object """


def is_kind_of_class(obj, a_class):
    """ Return True if object are instance of a class """

    if isinstance(obj, a_class):
        return True
    else:
        return False
