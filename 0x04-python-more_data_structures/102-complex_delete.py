#!/usr/bin/python3
def complex_delete(a_dictionary, value):
<<<<<<< HEAD
    for x in list(a_dictionary.keys()):
        if a_dictionary[x] is value:
            del a_dictionary[x]
=======
    if a_dictionary:
        for k, v in list(a_dictionary.items()):
            if v == value:
                del a_dictionary[k]
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
    return a_dictionary
