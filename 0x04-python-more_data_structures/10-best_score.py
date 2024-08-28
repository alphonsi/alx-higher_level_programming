#!/usr/bin/python3
def best_score(a_dictionary):
<<<<<<< HEAD
    if a_dictionary is None:
        return None
    maxval = 0
    maxkey = None
    for k, v in a_dictionary.items():
        if v > maxval:
            maxval = v
            maxkey = k
    return maxkey
=======
    if a_dictionary:
        return max(a_dictionary, key=a_dictionary.get)
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
