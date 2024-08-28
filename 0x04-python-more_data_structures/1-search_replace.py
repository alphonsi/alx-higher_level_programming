#!/usr/bin/python3
<<<<<<< HEAD
def search_replace(my_list, search, replace):
    return list(map(lambda e: replace if e == search else e, my_list))
=======
def search_replace(my_list, search replace):
    new_list = []
    for num in my_list:
        if num == search:
            new_list.append(replace)
        else:
            new_list.append(num)
    return new_list
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
