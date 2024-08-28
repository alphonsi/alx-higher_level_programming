#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list

<<<<<<< HEAD
    my_list_copy = my_list.copy()
    my_list_copy[idx] = element
    return my_list_copy
=======
    new_list = my_list[:]
    new_list[idx] = element
    return new_list
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
