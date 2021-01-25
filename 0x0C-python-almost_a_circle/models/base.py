#!/usr/bin/python3
""" Module to create a new class """


class Base:
    """ Base class is the first class """

    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id

        if id == None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
