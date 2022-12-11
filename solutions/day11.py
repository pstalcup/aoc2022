import re
from functools import reduce

def monkey(m):
    lines = m.split("\n")
    return dict(
        id=int(lines[0].split(":")[0]), 
        items=[int(n) for n in lines[1].split(":")[-1].split(",")], 
        operation=lines[2].split("=")[-1][1:], 
        test=int(re.search(r"divisible by (\d+)", lines[3])[1]), 
        t=int(lines[4][-1]), 
        f=int(lines[5][-1]),
        count=0
    )

def parse(s):
    return {m["id"]:m for m in [monkey(m) for m in s.split("Monkey")[1:]]}

def common(monkeys, op, n):    
    for i in range(n):
        for m in monkeys.values():
            items = m["items"]
            m["items"] = []
            m["count"] += len(items)
            for item in items:
                w = op(eval(m["operation"].replace("old", str(item))))
                if w % m["test"] == 0:
                    t = m["t"]
                else:
                    t = m["f"]
                monkeys[t]["items"] = monkeys[t]["items"] + [w]

    return reduce(lambda a,b: a * b, sorted(m["count"] for m in monkeys.values())[-2:])

def part1(s):
    return common(parse(s), lambda x: x // 3, 20)

def part2(s):
    monkeys = parse(s)    
    l = reduce(lambda a,b: a * b, [m["test"] for m in monkeys.values()])
    return common(monkeys, lambda x: x % l, 10000)