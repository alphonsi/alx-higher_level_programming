#!/usr/bin/python3
<<<<<<< HEAD
for i in range(10):
    for j in range(i, 10):
        if i < j:
            print("{:d}{:d}".format(i, j),
                  end="\n" if i is 8 and j is 9 else ", ")
=======
for i in range(0, 10):
    for j in range(1, 10):
        if i >= j:
            continue
        elif i == 8 and j == 9:
            print("{}{}".format(i, j))
        else:
            print("{}{}, ".format(i, j), end="")
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
