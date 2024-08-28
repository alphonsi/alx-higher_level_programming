#!/usr/bin/python3
def no_c(my_string):
<<<<<<< HEAD
    ret = ""
    for i in range(len(my_string)):
        if (my_string[i] != 'c' and my_string[i] != 'C'):
            ret += my_string[i]
    return ret
=======
    new_string = ""
    for letter in my_string:
        if letter != 'c' and letter != 'C':
            new_string += letter
    return new_string
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
