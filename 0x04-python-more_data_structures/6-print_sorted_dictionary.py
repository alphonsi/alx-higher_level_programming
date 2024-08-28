#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
<<<<<<< HEAD
    for k in sorted(a_dictionary.keys()):
        print("{}: {}".format(k, a_dictionary[k]))
=======
    for k, v in sorted(a_dictionary.items()):
        print("{}: {}".format(k, v))
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
