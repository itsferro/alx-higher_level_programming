#!/usr/bin/python3

def no_c(my_string):
    '''
        removes all characters c and C from a string.
    '''
    if my_string is not None:
        new_string = ""
        for i in my_string:
            if i != 'C' and i != 'c':
                new_string += i
        return str(new_string)
