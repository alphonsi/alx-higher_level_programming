#!/usr/bin/python3
def roman_to_int(roman_string):
<<<<<<< HEAD
    if not isinstance(roman_string, str):
        return 0
    total = 0
    num = 0
    digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for r in reversed(roman_string):
        num = digits[r]
        total += num if total < num * 5 else -num
    return total
=======
    if roman_string is None or type(roman_string) is not str:
        return 0
    int_sum = 0
    converter = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    for current, next in zip(roman_string, roman_string[1:]):
        if converter[current] >= converter[next]:
            int_sum += converter[current]
        else:
            int_sum -= converter[current]
    int_sum += converter[roman_string[-1]]
    return int_sum
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
