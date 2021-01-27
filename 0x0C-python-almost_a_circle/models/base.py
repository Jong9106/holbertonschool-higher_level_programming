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

    @classmethod
    def save_to_file(cls, list_objs):
        """ Class method to save in json file """

        if list_objs is None:
            new_list = []

        else:
            new_list = []
            for i in list_objs:
                new_list.append(cls.to_dictionary(i))
            new_list = Base.to_json_string(new_list)

        with open("{}.json".format(cls.__name__), 'w') as new_file:

            import json

            new_file.write(new_list)

    @staticmethod
    def from_json_string(json_string):
        """ Static method to return a string representation from a json file"""

        if json_string is None or not json_string:
            return []

        import json

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Class method to create a instance with attributes setted"""

        dummy_instance = cls(1, 1, 1)
        cls.update(dummy_instance, **dictionary)
        return dummy_instance
