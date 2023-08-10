#!/usr/bin/python3
for char in range(ord('a'), ord('z') + 1):
    if char is ord('e') or char is ord('q'):
        continue
    print("{:c}".format(char), end='')
