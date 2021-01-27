#!/usr/bin/python3
""" Module to create a new class """


class Base:
    """ Base class is the first class """

    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id

        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ static method to return a json string representation """

        import json

        if list_dictionaries is None or not list_dictionaries:
            return json.dumps([])

        return json.dumps(list_dictionaries)
