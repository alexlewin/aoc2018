#!/usr/bin/env python

from collections import Counter


def has2s_has3s(string):
    counts = Counter(string)
    values = counts.values()
    return 2 in values, 3 in values


wordswith2s = 0
wordswith3s = 0

for line in open('input'):
    word = line.rstrip()
    has2s, has3s = has2s_has3s(word)
    wordswith2s += int(has2s)
    wordswith3s += int(has3s)

checksum = wordswith2s * wordswith3s
print(checksum)

