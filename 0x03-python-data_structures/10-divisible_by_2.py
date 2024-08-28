#!/usr/bin/python3
def divisible_by_2(my_list=[]):
<<<<<<< HEAD
    return list(map(lambda x: True if x % 2 == 0 else False, my_list))
=======
    new_list = []
    for num in my_list:
        if num % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
