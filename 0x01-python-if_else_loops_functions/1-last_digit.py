#!/usr/bin/python3
import random
<<<<<<< HEAD
import math
number = random.randint(-10000, 10000)
mod = number % 10 if number > 10 else number % -10
print(
    "Last digit of {:d} is {:d} and is "
    .format(number, mod), end="")
if mod > 5:
    print("greater than 5")
elif mod == 0:
    print("0")
else:
    print("less than 6 and not 0")
=======
number = random.randint(-10000, 10000)
last = number % 10
if last > 5:
    print("Last digit of", number, "is", last, "and is greater than 5")
elif last == 0:
    print("Last digit of", number, "is", last, "and is 0")
elif last < 6 and last != 0:
    print("Last digit of", number, "is", last, "and is less than 6 and not 0")
else:
    print(last)
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
