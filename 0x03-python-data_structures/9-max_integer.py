#!/usr/bin/python3
def max_integer(my_list=[]):
<<<<<<< HEAD
    if len(my_list) < 1:
        return None
    list_copy = my_list.copy()
    list_copy.sort()
    return list_copy[-1]
=======
    if my_list:
        max = my_list[0]
        for num in my_list:
            if num >= max:
                max = num
        return max
    else:
        return None
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
