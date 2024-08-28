#!/usr/bin/python3
<<<<<<< HEAD
if __name__ == "__main__":
    import hidden_4
    for l in dir(hidden_4):
        if l[0:2] != "__":
            print(l)
=======
import hidden_4

if __name__ == "__main__":
    for str in dir(hidden_4):
        if str[:2] != "__":
            print("{}".format(str))
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
