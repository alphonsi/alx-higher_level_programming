#!/usr/bin/python3
import random
number = random.randint(-10, 10)
<<<<<<< HEAD
if number > 0:
    print("{:d} is positive".format(number))
elif number < 0:
    print("{:d} is negative".format(number))
else:
    print("{:d} is zero".format(number))
=======
if number < 0:
    print(number, "is negative")
elif number == 0:
    print(number, "is zero")
else:
    print(number, "is positive")
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
