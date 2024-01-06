#!/usr/bin/python3

for i in range(26):
    if i % 2 == 0:
        char = ord('z') - i
    else:
        char = ord('Z') - i
    print("{}".format(chr(char)), end="")
