#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
<<<<<<< HEAD
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (a1 + b1, a2 + b2)
=======
    a = tuple_a or (0, 0)
    b = tuple_b or (0, 0)
    if len(tuple_a) == 1:
        a = (tuple_a[0], 0)
    if len(tuple_b) == 1:
        b = (tuple_b[0], 0)
    new = (a[0] + b[0], a[1] + b[1])
    return new
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
