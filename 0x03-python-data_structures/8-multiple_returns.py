#!/usr/bin/python3
def multiple_returns(sentence):
<<<<<<< HEAD
    return (len(sentence), sentence[0] if len(sentence) > 0 else None)
=======
    if sentence:
        new = (len(sentence), sentence[0])
    else:
        new = (0, None)
    return new
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
