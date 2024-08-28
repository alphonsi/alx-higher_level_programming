#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
<<<<<<< HEAD
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
=======
    if my_list:
        if 0 <= idx < len(my_list):
            del my_list[idx]
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
    return my_list
