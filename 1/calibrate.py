#!/usr/bin/env python

import sys


state = 0
for line in open('input'):
    state += int(line)

print('after all lines:', state)


#####


state = 0
seen = set([state])

while True:
    for line in open('input'):
        state += int(line)
        if state in seen:
           print('first repeated:', state)
           exit(0)
        seen.add(state)
