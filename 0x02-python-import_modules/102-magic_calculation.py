#!/usr/bin/python3
<<<<<<< HEAD
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
=======
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
<<<<<<< HEAD
    else:
        return sub(a, b)
    return 0
=======

    else:
        return sub(a, b)
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
