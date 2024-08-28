#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
<<<<<<< HEAD
    i = 0
    ret = []
    while i < list_length:
        res = 0
        try:
            res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            ret.append(res)
            i += 1
    return ret
=======
    new_list = []
    for i in range(list_length):
        quotient = 0
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(quotient)
    return new_list
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
