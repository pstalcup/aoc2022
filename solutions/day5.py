import re

def clean(l):
    return re.sub(r"[ \[](.)[ \]] ",r"\1", l + " ")

def stack(crates):
    return [[c[i] for c in reversed(crates) if c[i] != " "] for i in range(len(crates[0]))]

def shared(s):
    lines = s.split("\n")
    height = len([l for l in lines if "[" in l])

    crates = [[]] + stack([clean(l) for l in lines[0:height]])

    command_re = re.compile(r"move (\d+) from (\d+) to (\d+)")
    commands = [[int(c[1]), int(c[2]), int(c[3])] for c in [re.match(command_re, l) for l in lines if re.match(command_re, l)]]

    return [crates, commands]
    

def part1(s):
    crates, commands = shared(s)

    for qty, src, dest in commands:
        for q in range(qty):
            crates[dest] = crates[dest] + crates[src][-1:]
            crates[src] = crates[src][:-1]

    return "".join(c[-1] for c in crates if len(c) > 0)

def part2(s):
    crates, commands = shared(s)

    for qty, src, dest in commands:
        crates[dest] = crates[dest] + crates[src][-qty:]
        crates[src] = crates[src][:-qty]

    return "".join(c[-1] for c in crates if len(c) > 0)