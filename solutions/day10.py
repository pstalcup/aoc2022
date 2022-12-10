from functools import reduce
from itertools import chain

def shared(s):
    ops = chain.from_iterable([[0] if l[0] == "n" else [0, int(l[5:])] for l in s.split("\n")[:-1]])
    return reduce(lambda l,v: l + [l[-1] + v], ops, [1])

def part1(s):
    register = shared(s)
    return sum(register[20 + 40 * n - 1] * (20 + 40 * n) for n in range(6))

def part2(s):
    f = "".join(["#" if a % 40 in [s - 1, s, s + 1] else "." for a, s in enumerate(shared(s))])
    return "\n".join(["", *[f[n * 40:(n + 1) * 40] for n in range(6)]])