#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    '''
        takes a list, index, and an element
        and replaces the old element at index
        to the element passed
        returns a modified list.
    '''
    my_list_length = len(my_list)
    if idx < 0 or idx >= my_list_length or my_list_length == 0:
        return my_list
    my_list[idx] = element
    return my_list
