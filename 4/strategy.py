#!/usr/bin/env python

import re
import sys
from collections import defaultdict


naps = defaultdict(lambda: defaultdict(int))

def register_nap(guard, sleeps, wakes):
    for minute in range(sleeps, wakes):
        naps[guard][minute] += 1


lines = sorted(open('input').readlines())
for line in lines:
    m = re.search(r'\d\d:(\d\d)\] Guard #(\d+) begins shift', line)
    if m:
        guard = int(m.group(2))
        continue

    m = re.search(r'\d\d:(\d\d)\] falls asleep', line)
    if m:
        sleeps = int(m.group(1))
        continue

    m = re.search(r'\d\d:(\d\d)\] wakes up', line)
    if m:
        wakes = int(m.group(1))
        register_nap(guard, sleeps, wakes)
        continue

    print('parse error!')
    sys.exit(1)


# Strategy 1: sleepiest minute of sleepiest guard
guard = max(
    (sum(naps[guard].values()), guard)
    for guard in naps.keys()
)[1]
print('sleepiest guard: {}'.format(guard))
minute = max(
    (count, minute)
    for minute, count in naps[guard].items()
)[1]
print('sleepiest minute for sleepiest guard: {}'.format(minute))
print('product: {}'.format(guard * minute))


# Strategy 2: globally sleepiest minute
freq, minute, guard = max(
    (freq, minute, guard)
    for guard, minutes in naps.items()
    for minute, freq in minutes.items()
)
print('sleepist guard and minute: {}, {}'.format(guard, minute))
print('product: {}'.format(guard * minute))
