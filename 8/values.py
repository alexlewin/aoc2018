#!/usr/bin/env python


entries = [int(n) for n in open('input').read().split()]


def node_value(i):
    """Returns (new i, value)"""
    value = 0

    num_kids = entries[i]
    i += 1
    num_meta = entries[i]
    i += 1

    kid_value = {}
    for kid_index in range(1, num_kids + 1):
        i, value = node_value(i)
        kid_value[kid_index] = value

    value = 0
    for _ in range(num_meta):
        entry = entries[i]
        if num_kids == 0:
            value += entry
        else:
            value += kid_value.get(entry, 0)
        i += 1

    return i, value


print(node_value(0))
