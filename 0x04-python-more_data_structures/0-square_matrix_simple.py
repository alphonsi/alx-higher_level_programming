#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
<<<<<<< HEAD
    return list(map(lambda submat: list(map(lambda e: e**2, submat)), matrix))
=======
    new_matrix = []
    for i in matrix:
        new_matrix.append(list(map(lambda x: x ** 2, i)))
    return new_matrix
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
