#!/usr/bin/python3
def remove_char_at(str, n):
    tam = len(str)
    arr = ""
    for i in range(tam):
        if (i != n):
            arr = arr + str[i]
    return (arr)
