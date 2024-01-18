#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    '''
        prints all integers of a list, in reverse order.
    '''
    if my_list:
        reversed_list = [my_list[x - 1] for x in range(len(my_list), 0, -1)]
        for i in reversed_list:
            print('{:d}'.format(i))
