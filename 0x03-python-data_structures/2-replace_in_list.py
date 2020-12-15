#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    cont = len(my_list)
    if idx < 0 and cont < idx:
        return my_list
    for str in range(cont):
        if str == idx:
            my_list[idx] = element
            return my_list
