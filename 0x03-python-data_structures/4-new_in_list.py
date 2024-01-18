#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    '''
        replaces an element in a list at a specific position
        without modifying the original list (like in C).
    '''
    list_len = len(my_list)
    new_list = my_list[:]
    if idx < 0 or idx >= list_len or list_len == 0:
        return new_list
    new_list[idx] = element
    return new_list
