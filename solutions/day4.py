def between(a, low, high):
    return low <= a and a <= high

def part1(s):
    pairs = [[[int(n) for n in p.split("-")] for p in l.split(",")] for l in s.split("\n")[:-1]]
    count = 0
    for pair in pairs:
        if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
            count += 1
        
        elif pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1]:
            count += 1
    return count

def part2(s):
    pairs = [[[int(n) for n in p.split("-")] for p in l.split(",")] for l in s.split("\n")[:-1]]
    count = 0
    for a in pairs:
        if between(a[0][0], a[1][0], a[1][1]) or between(a[0][1], a[1][0], a[1][1]):
            count += 1
        
        elif between(a[1][0], a[0][0], a[0][1]) or between(a[1][1], a[0][0], a[0][1]):
            count += 1
    return count