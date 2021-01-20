#!/usr/bin/python3
""" Fucntion to check if a object is istance of a class """


def inherits_from(obj, a_class):
    """ Return True if object are instance of a class """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
