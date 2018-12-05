#!/usr/bin/env python

from itertools import zip_longest


def diffmask(box1, box2):
    return [let1 != let2 for let1, let2 in zip_longest(box1, box2)]


boxes = [line.rstrip() for line in open('input')]

for i, box1 in enumerate(boxes):
    for box2 in boxes[i+1:]:
        mask = diffmask(box1, box2)
        if sum(mask) == 1:
            position = mask.index(True)
            print(box1[:position] + box1[position+1:])
            exit(0)

