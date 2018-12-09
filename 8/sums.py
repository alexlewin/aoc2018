#!/usr/bin/env python


entries = [int(n) for n in open('input').read().split()]


def sum_of_meta(i):
    """Returns (new i, meta_sum)"""
    meta_sum = 0

    num_kids = entries[i]
    i += 1
    num_meta = entries[i]
    i += 1

    for _ in range(num_kids):
        i, meta = sum_of_meta(i)
        meta_sum += meta

    for _ in range(num_meta):
        meta_sum += entries[i]
        i += 1

    return i, meta_sum


print(sum_of_meta(0))
