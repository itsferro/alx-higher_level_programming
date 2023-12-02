#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    numbers = argv[1:]

    result = 0
    for i in range(len(numbers)):
        result = result + int(numbers[i])

    print("{}".format(result))
