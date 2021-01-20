#!/usr/bin/python3
""" Module to create a function """

import json


def to_json_string(my_obj):
    """ Function that returns the JSON representation of an object """

    return json.dumps(my_obj)
