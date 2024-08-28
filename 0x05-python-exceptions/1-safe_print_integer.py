#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
<<<<<<< HEAD
    except:
        return False
    return True
=======
        return True
    except (ValueError, TypeError):
        return False
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
