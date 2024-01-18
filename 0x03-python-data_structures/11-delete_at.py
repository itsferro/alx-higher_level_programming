#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    '''
        deletes the item at a specific position in a list.
    '''
    new_list = []
    if my_list:
        list_len = len(my_list)
        if idx >= 0 and idx < list_len:
            for i in range(list_len):
                if i >= idx and i < (list_len - 1):
                    my_list[i] = my_list[i + 1]
            del my_list[i]

    return my_list
