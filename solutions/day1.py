def shared(s):
    return sorted([sum(int(n) for n in x.split("\n") if n != "") for x in s.split("\n\n")], reverse=True)

def part1(s):
    v = shared(s)
    return v[0]

def part2(s):
    v = shared(s)
    return sum(v[0:3])