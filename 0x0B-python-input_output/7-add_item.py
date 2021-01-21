#!/usr/bin/python3
"""
Module to create a scrip that adds all arguments to a Python list,
and then save them to a file
"""

from sys import argv as av

save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

new_file = "add_item.json"

try:
    new_list = load(new_file)

except:
    new_list = []

for i in av[1:]:
    new_list.append(i)
save(new_list, new_file)
