#!/usr/bin/python3
<<<<<<< HEAD
for i in range(100):
    print("{:02d}".format(i), end="\n" if i == 99 else ", ")
=======
for int in range(0, 100):
    if int != 99:
        print("{:02d}, ".format(int), end="")
    else:
        print("{:02d}".format(int))
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
