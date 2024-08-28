#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
<<<<<<< HEAD
        while i is not x:
            print(my_list[i], end='')
            i += 1
    except IndexError:
        None
    print()
=======
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            i += 1
        print("")
    except IndexError:
        print("")
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
    return i
