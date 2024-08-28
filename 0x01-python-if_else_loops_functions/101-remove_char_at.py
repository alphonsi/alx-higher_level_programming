#!/usr/bin/python3
def remove_char_at(str, n):
<<<<<<< HEAD
    newstr = ""
    for i, c in enumerate(str):
        if i != n:
            newstr += c
    return newstr
=======
    newStr = ""
    for i in range(len(str)):
        if i == n:
            continue
        else:
            newStr += str[i]
    return newStr
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
