#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    '''
        finds all multiples of 2 in a list.
    '''
    list_result = []
    if my_list:
        list_len = len(my_list)
        for i in range(list_len):
            if (my_list[i] % 2) == 0:
                list_result.append(True)
            else:
                list_result.append(False)
        return list_result
    else:
        return None
