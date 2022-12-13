import json
import itertools

def cmp(a, b):
    alist = isinstance(a, list)
    blist = isinstance(b, list)

    if not alist and not blist:
        return a - b
    if alist and blist:
        if len(a) == 0 or len(b) == 0:
            return len(a) - len(b)
        f = cmp(a[0], b[0])
        if f == 0:
            return cmp(a[1:], b[1:])
        else:
            return f
        return cmp(a[0], b[0])
    elif alist and not blist:
        return cmp(a, [b])
    else:
        return cmp([a], b)


def part1(s):
    pairs = [[json.loads(l) for l in p.split("\n") if l != ""] for p in s.split("\n\n")]
    return sum(i + 1 for i, pair in enumerate(pairs) if cmp(*pair) < 0)


def part2(s):
    inst = [json.loads(l) for l in s.split("\n") if l != ""]
    return (len([1 for p in inst if cmp(p, [[2]]) <= 0]) + 1) * (len([p for p in inst if cmp(p, [[6]]) <= 0]) + 2)