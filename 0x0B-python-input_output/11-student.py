#!/usr/bin/python3
""" Module to create a new class """


class Student:
    """ Class Studen to define by, first name, last name and age """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for i, j in self.__dict__.items():
                if i in attrs:
                    new_dict[i] = j
            return new_dict

    def reload_from_json(self, json):
        for i, j in json.items():
            setattr(self, i, j)
