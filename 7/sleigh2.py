#!/usr/bin/env python

from collections import defaultdict
from itertools import count
import re
import string


NUM_WORKERS = 5
TIMING_OFFSET = 60

LETTER_VALUES = range(TIMING_OFFSET + 1, TIMING_OFFSET + 27)

LETTER_TIMING = dict(zip(string.ascii_uppercase, LETTER_VALUES))


dependencies = defaultdict(set)

            
for line in open('input'):
    m = re.search(r'(\w) must be finished before step (\w)', line)
    dep, letter = m.groups()
    dependencies[letter].add(dep)
    dependencies[dep].update()


worker_timing = [0] * NUM_WORKERS
worker_letter = [None] * NUM_WORKERS


for t in count():
    done_workers = []
    for worker in range(len(worker_timing)):
        if worker_timing[worker] > 0:
            worker_timing[worker] -= 1
        if worker_timing[worker] == 0:
            done_workers.append(worker)

    for worker in done_workers:
        done_letter = worker_letter[worker]
        worker_letter[worker] = None

        if done_letter is not None:
            print(done_letter, end='')
            for deps in dependencies.values():
                deps.discard(done_letter)

    next_letters = sorted(letter for letter, deps in dependencies.items() if not deps)

    while done_workers and next_letters:
        worker = done_workers.pop(0)
        letter = next_letters.pop(0)
        del dependencies[letter]
        worker_letter[worker] = letter
        worker_timing[worker] = LETTER_TIMING[letter]

    if set(worker_timing) == {0} and not next_letters:
        break

print()
print(t)
