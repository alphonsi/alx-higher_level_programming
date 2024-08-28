#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
<<<<<<< HEAD
    if not my_list:
        return None
    for i in reversed(my_list):
        print("{:d}".format(i))
=======
    if my_list:
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
