#!/usr/bin/python3
def square_matrix_map(matrix=[]):
<<<<<<< HEAD
    return list(map(lambda submat: list(map(lambda e: e**2, submat)), matrix))
=======
    return list(map(lambda x: list(map(lambda y: y ** 2, x)), matrix))
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
