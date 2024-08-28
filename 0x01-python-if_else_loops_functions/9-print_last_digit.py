#!/usr/bin/python3
def print_last_digit(number):
<<<<<<< HEAD
    number = abs(number) % 10
    print(number, end="")
    return number
=======
    last = abs(number) % 10
    print("{}".format(last), end="")
    return last
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
