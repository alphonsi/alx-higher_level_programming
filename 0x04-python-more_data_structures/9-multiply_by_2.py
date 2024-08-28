#!/usr/bin/python3
def multiply_by_2(a_dictionary):
<<<<<<< HEAD
    return {k: v * 2 for k, v in a_dictionary.items()}
=======
    new = dict()
    for k, v in a_dictionary.items():
        new[k] = v * 2
    return new9-multiply_by_2b
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
