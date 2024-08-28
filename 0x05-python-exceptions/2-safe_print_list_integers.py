#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
<<<<<<< HEAD
    i, c = 0, 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end='')
            c += 1
        except (ValueError, TypeError):
            pass
        i += 1
    print()
    return c
=======
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return count
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
