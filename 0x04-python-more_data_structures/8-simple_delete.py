#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
<<<<<<< HEAD
    if a_dictionary.get(key) is not None:
=======
    if key in a_dictionary:
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
        del a_dictionary[key]
    return a_dictionary
