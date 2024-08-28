#!/usr/bin/python3
<<<<<<< HEAD
if __name__ == "__main__":
    import sys
    l = len(sys.argv) - 1
    print("{} argument{}{}"
          .format(l, "" if l == 1 else "s", "." if l == 0 else ":"))
    for i in range(l):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
=======
from sys import argv

if __name__ == "__main__":
    length = len(argv) - 1
    if length == 0:
        print("{}".format("0 arguments."))
    elif length == 1:
        print("{}".format("1 argument:"))
        print("1: {}".format(argv[1]))
    else:
        print("{:d} {}".format(length, "arguments:"))
        for i in range(1, length + 1):
            print("{:d}: {}".format(i, argv[i]))
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
