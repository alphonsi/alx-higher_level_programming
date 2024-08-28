#!/usr/bin/python3
def safe_print_division(a, b):
    try:
<<<<<<< HEAD
        a = a / b
    except ZeroDivisionError:
        a = None
    finally:
        print("Inside result:", "{}".format(a))
    return a
=======
        quot = a / b
    except ZeroDivisionError:
        quot = None
    finally:
        print("Inside result: {}".format(quot))
    return quot
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
