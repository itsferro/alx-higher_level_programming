#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    '''
        adds 2 tuples.
    '''
    new_tuple = []
    tuple_a = list(tuple_a)
    tuple_b = list(tuple_b)
    tuple_a_len = len(tuple_a)
    tuple_b_len = len(tuple_b)
    if tuple_a_len < 2:
        if tuple_a_len == 1:
            tuple_a += (0, )
        else:
            tuple_a = [0, 0]

    if tuple_b_len < 2:
        if tuple_b_len == 1:
            tuple_b += (0, )
        else:
            tuple_b = [0, 0]

    new_tuple.append(tuple_a[0] + tuple_b[0])
    new_tuple.append(tuple_a[1] + tuple_b[1])

    return tuple(new_tuple)
