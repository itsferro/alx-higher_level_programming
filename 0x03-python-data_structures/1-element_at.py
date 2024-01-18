#!/usr/bin/python3

def element_at(my_list, idx):
    '''
        takes a list and index
        returns element at index.
    '''
    my_list_length = len(my_list)
    if idx < 0 or idx >= my_list_length or my_list_length == 0:
        return none
    return my_list[idx]
