from functools import reduce

def shared(s):
    rows = [[int(n) for n in r] for r in s.split("\n")[:-1]]
    rrows = [list(reversed(r)) for r in rows]
    cols = [[r[i] for r in rows] for i in range(len(rows[0]))]
    rcols = [list(reversed(c)) for c in cols]

    return rows, rrows, cols, rcols

def visible(l):
    return max(l) == l[-1] and l[-1] not in l[:-1]

def part1(s):
    rows, rrows, cols, rcols = shared(s)

    count = 0

    for r in range(1, len(rows) - 1):
        for c in range(1, len(rows[r]) - 1):
            if visible(rows[r][:c + 1]) or visible(cols[c][:r + 1]) or visible(rrows[r][:-c]) or visible(rcols[c][:-r]):
                count += 1

    return count + len(rows) * 2 + len(cols) * 2 - 4

def scenic(l):
    r = reduce(lambda a, i: (True, 1 + a[1]) if a[0] and i < l[-1] else a, reversed(l[:-1]), (True, 1))[1]
    return r

def seen(v):
    def f(l):
        if len(l) == 0:
            return 0
        elif l[-1] >= v:
            return 1
        else:
            return 1 + f(l[:-1])
    return f

def part2(s):
    rows, rrows, cols, rcols = shared(s)

    score = 0

    for r in range(1, len(rows) - 1):
        for c in range(1, len(rows[r]) - 1):
            f = seen(rows[r][c])
            v = [f(rows[r][:c]), f(cols[c][:r]), f(rrows[r][:-(c + 1)]), f(rcols[c][:-(r + 1)])]
            score = max(score, reduce(lambda a, b: a * b, v, 1))
    
    return score