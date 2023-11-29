#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) in range(ord('a'), ord('z') + 1):
            upper = chr(ord(str[i]) - 32)
        else:
            upper = str[i]
        print("{}".format(upper), end="")
    print("")
