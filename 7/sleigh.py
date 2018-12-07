#!/usr/bin/env python


from collections import defaultdict
import re


dependencies = defaultdict(set)

            
for line in open('input'):
    m = re.search(r'(\w) must be finished before step (\w)', line)
    dependency, node = m.groups()
    dependencies[node].add(dependency)
    dependencies[dependency].update()


while True:
    next_node = min((node for node, deps in dependencies.items() if not deps), default=None)
    if not next_node:
        break

    print(next_node, end='')

    del dependencies[next_node]
    for deps in dependencies.values():
        deps.discard(next_node)


print()
