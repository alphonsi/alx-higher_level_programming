#!/usr/bin/python3
def weight_average(my_list=[]):
<<<<<<< HEAD
    return sum([x[0] * x[1] for x in my_list]) / \
        (sum([x[1] for x in my_list]) or 1)
=======
    points = 0
    total = 0
    if my_list:
        tup = ()
        for tup in my_list:
            points += (tup[0] * tup[1])
            total += tup[1]
        return points / total
    return 0
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
