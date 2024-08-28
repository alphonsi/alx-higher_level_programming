#!/usr/bin/python3
<<<<<<< HEAD
def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False


def uppercase(str):
    for c in str:
        print("{:c}"
              .format(ord(c) if not islower(c) else ord(c) - 32),
              end="")
    print("")
=======
def uppercase(str):
    for i in range(len(str)):
        char = ord(str[i])
        if char >= 97 and char <= 122:
            char = char - 32
            print("{}".format(chr(char)), end="")
    print()
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
