from functools import reduce
from itertools import zip_longest 
import re

UPPER_ASCII_START = 65
LOWER_ASCII_START = 97
priority = [0] + [chr(c) for c in [*range(LOWER_ASCII_START, LOWER_ASCII_START + 26), *range(UPPER_ASCII_START, UPPER_ASCII_START + 26)]]

def common(*items):
    return reduce(lambda a, b: a.intersection(b), [set(i) for i in items])

def halves(l):
    return [l[:len(l)//2], l[len(l)//2:]]


def chunk(l, n):
    args = [iter(l)] * n
    return zip_longest(*args)

def part1(s):
    lines = [l for l in s.split("\n") if l != ""]
    parts = [common(*halves(l)) for l in lines]

    return sum(sum(priority.index(c) for c in p) for p in parts)

def part2(s):
    lines = s.split("\n")[:-1]
    # groups = []
    # group = []

    # for i in range(1, len(lines) + 1):
    #   group = group + [lines[i - 1]]
    #    if i % 3 == 0:
    #        groups = groups + [group]
    #        group = []
    
    groups = chunk(lines, 3)
    parts = [common(*g) for g in groups]
    return sum(sum(priority.index(c) for c in p ) for p in parts)
