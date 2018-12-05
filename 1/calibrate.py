#!/usr/bin/env python

import sys


state = 0
seen = set([state])

while True:
    for line in open('input'):
        print(state)
        state += int(line)
        if state in seen:
           print(state)
           exit(0)
        seen.add(state)
