#!/usr/bin/python3
<<<<<<< HEAD
from __future__ import print_function
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
=======
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as error:
        sys.stderr.write("Exception: {}\n".format(error))
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
        return None
