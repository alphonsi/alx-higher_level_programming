#!/usr/bin/python3
<<<<<<< HEAD
for i in range(25, -1, -1):
    c = i + ord('A')
    if i % 2 == 1:
        c += 32
    print("{:c}".format(c), end="")
=======
for i in range(122, 96, -1):
    if i % 2 == 0:
        n = chr(i)
    else:
        n = chr(i-32)
    print("{}".format(n), end="")
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
