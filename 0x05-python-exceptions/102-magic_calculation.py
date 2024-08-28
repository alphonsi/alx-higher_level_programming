#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
<<<<<<< HEAD
            else:
                result += a ** b / i
        except:
            result = b + a
=======
            result += a ** b / i
        except:
            result = a + b
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
            break
    return result
