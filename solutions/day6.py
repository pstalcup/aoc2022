from functools import reduce

def find_unique(s, n):
    return [i + n for i in range(len(s) - n) if len(set(s[i:i+n])) == n][0]

def part1(s):
    return find_unique(s, 4)

def part2(s):
    return find_unique(s, 14)