#!/usr/bin/env python

import sys
from collections import defaultdict


def react(p):
    # Walk through polymer left to right.
    # If find a pair, react, then move back one in case there is a new pair.
    # Otherwise, move forwards.
    # Repeat until fall off end.
    #
    i = 0
    try:
        while True:
            pi = p[i]
            pi1 = p[i+1]
            if pi != pi1 and pi.lower() == pi1.lower():
                p = p[:i] + p[i+2:]
                if i > 0:
                    i -= 1
            else:
                i += 1

    except IndexError:
        # Done
        pass

    return p


def remove_unit(p, unit):
    return p.translate(str.maketrans({unit.lower(): None, unit.upper(): None}))


polymer = open('input').read().rstrip()


reacted_polymer = react(polymer)
print('reacted polymer length: {}'.format(len(reacted_polymer)))


reacted_polymer_length_without_unit = defaultdict(int)
for unit in set(polymer.lower()):
    reacted_polymer_length_without_unit[unit] = len(react(remove_unit(polymer, unit)))
leng, unit = min((leng, unit) for unit, leng in reacted_polymer_length_without_unit.items())
print('shortest is {} by removing {}'.format(leng, unit))


