#!/usr/bin/python3
<<<<<<< HEAD
from __future__ import print_function
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
=======
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as error:
        sys.stderr.write("Exception: {}\n".format(error))
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
        return False
