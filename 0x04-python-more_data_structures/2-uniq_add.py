#!/usr/bin/python3
def uniq_add(my_list=[]):
<<<<<<< HEAD
    return sum(set(my_list))
=======
    sum = 0
    my_set = set(my_list)
    for num in my_set:
        sum += num
    return sum
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
