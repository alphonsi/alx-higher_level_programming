#!/usr/bin/python3
def show_chars():
    for char in range(ord('a'), ord('z') + 1):
        print(chr(char), end='')


if __name__ == "__main__":
    show_chars()
