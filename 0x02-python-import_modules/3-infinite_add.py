#!/usr/bin/python3
<<<<<<< HEAD
if __name__ == "__main__":
    import sys
    sum = 0
    for i in range(len(sys.argv) - 1):
        sum += int(sys.argv[i + 1])
    print(sum)
=======
from sys import argv

if __name__ == "__main__":
    length = len(argv)
    sum = 0
    for i in range(1, length):
        sum += int(argv[i])
    print("{:d}".format(sum))
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
