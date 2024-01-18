#!/usr/bin/python3

def max_integer(my_list=[]):
    '''
        finds the biggest integer of a list.
    '''
    if my_list:
        list_len = len(my_list)
        n = my_list[0]
        for i in range(list_len):
            if n < my_list[i]:
                n = my_list[i]

        return n
    else:
        return None
