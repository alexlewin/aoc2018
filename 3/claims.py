#!/usr/bin/env python

from collections import defaultdict
import re


claims = set()
claimed_squares = defaultdict(list)

for line in open('input'):
    # scanf would have been easier...
    matches = re.match(r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
    claimno, x0, y0, width, height = matches.groups()

    claims.add(claimno)
    x0int = int(x0)
    y0int = int(y0)
    widthint = int(width)
    heightint = int(height)

    for x in range(x0int, x0int + widthint):
        for y in range(y0int, y0int + heightint):
            claimed_squares[(x, y)].append(claimno)

num_disputed_squares = sum(len(claimlist) > 1 for claimlist in claimed_squares.values())
print(num_disputed_squares)

undisputed_claims = claims.copy()
for claimlist in claimed_squares.values():
    if len(claimlist) > 1:
        for claimer in claimlist:
            undisputed_claims.discard(claimer)
print(undisputed_claims)

