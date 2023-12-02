#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arguments = argv[1:]
    arglen = len(arguments)
    if arglen == 0:
        print("{} arguments.".format(arglen))
    elif arglen == 1:
        print("{} argument:".format(arglen))
    else:
        print("{} arguments:".format(arglen))

    for i in range(arglen):
        print("{}: {}".format(i + 1, arguments[i]))
