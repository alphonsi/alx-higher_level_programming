#!/usr/bin/python3
<<<<<<< HEAD
for i in range(ord('a'), ord('z') + 1):
    if i != ord('q') and i != ord('e'):
        print("{:c}".format(i), end="")
=======
for char in range(ord('a'), ord('z') + 1):
    if char is ord('e') or char is ord('q'):
        continue
    print("{:c}".format(char), end='')
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
