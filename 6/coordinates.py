#!/usr/bin/env python


from collections import defaultdict, Counter


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def tuple(self):
        return (self.x, self.y)

    def __repr__(self):
        return '({}, {})'.format(*self.tuple)

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __sub__(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)


class Grid(defaultdict):
    def yiter(self):
        return range(self.ymin, self.ymax + 1)

    def xiter(self):
        return range(self.xmin, self.xmax + 1)

    def __repr__(self):
        repr = ''
        for y in self.yiter():
            for x in self.xiter():
                repr += self.get(Point(x, y), ' ')
            repr += '\n'
        return repr

    @property
    def xmin(self):
        return min(p.x for p in self.keys())

    @property
    def xmax(self):
        return max(p.x for p in self.keys())

    @property
    def ymin(self):
        return min(p.y for p in self.keys())

    @property
    def ymax(self):
        return max(p.y for p in self.keys())

    @property
    def counts(self):
        return Counter(self.values())

    @property
    def values_on_boundaries(self):
        return set(self[Point(x, y)] for x in (self.xmin, self.xmax) for y in self.yiter()) \
            | set(self[Point(x, y)] for y in (self.ymin, self.ymax) for x in self.xiter())

    @property
    def counts_excluding_boundaries(self):
        counts = self.counts
        for value in self.values_on_boundaries:
            del counts[value]
        return counts


# Original input
originals = Grid()
for i, line in enumerate(open('input')):
    x, y = line.rstrip().split(', ')
    originals[Point(int(x), int(y))] = str(i)


def find_closest(point):
    sorted_dists = sorted((orig - point, i, orig) for orig, i in originals.items())
    if sorted_dists[0][0] == sorted_dists[1][0]:
        return '.'
    else:
        return sorted_dists[0][1]


def total_distance(point):
    return sum(orig - point for orig in originals.keys())


# For each point within bounds, find_closest and total_distance
closest = Grid()
distance = Grid()
for y in originals.yiter():
    for x in originals.xiter():
        point = Point(x, y)
        closest[point] = find_closest(point)
        distance[point] = total_distance(point)

        if not len(closest) % 1000:
            print('done %s' % len(closest))

print('counts are %s' % closest.counts)
print('values on boundaries are %s' % closest.values_on_boundaries)
print('counts minus boundaries are %s' % closest.counts_excluding_boundaries)


# We are assuming here that none of the 10000 region will be outside the bounds
# of the original points. For our given data, this happens to be true. HACK LAZY
print('sub-10000 region size is %s' % sum(1 for d in distance.values() if d < 10000))

