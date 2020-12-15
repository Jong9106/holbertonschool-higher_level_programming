#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        copy_list = my_list.copy()
        cont = len(copy_list)
        if idx < 0 or idx >= cont:
            return copy_list
        copy_list[idx] = element
        return copy_list
