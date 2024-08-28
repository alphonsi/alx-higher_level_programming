#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        return c
<<<<<<< HEAD
    if c > b:
        return a + b
=======
    elif c > b:
        return a + b

>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
    return a * b - c
