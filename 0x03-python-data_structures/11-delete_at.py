#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    size = len(my_list)
    if idx >= size or idx < 0:
        return my_list
    my_list.remove(idx + 1)
    return my_list
