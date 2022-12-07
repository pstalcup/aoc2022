def dig(root, path):
    if len(path) > 0:
        return dig(root[path[0]], path[1:])
    return root

def parse(inputs):
    root = {}
    path = []

    for input in inputs:
        s = input.split("\n")
        cmd = s[0].split(" ")
        
        if cmd[0] == "cd":
            if cmd[1] == "..":
                path = path[:-1]
            elif cmd[1] != "/":
                path = path + [cmd[1]]
        if s[0][:2] == "ls":
            pwd = dig(root, path)
            for desc in s[1:-1]:
                size, name = desc.split(" ")
                if size == "dir":
                    pwd[name] = {}
                else:
                    pwd[name] = int(size)
    return root

def size(root, path):
    sizes = {}
    computed = 0
    for k in root:
        if isinstance(root[k], dict):
            total, subsizes = size(root[k], f"{path}/{k}")
            computed += total
            sizes = {**sizes, **subsizes}
        else:
            computed += root[k]
    return computed, {path: computed, **sizes}

def part1(s):
    total, sizes = size(parse(s.split("$ ")), "")
    return sum(s for s in sizes.values() if s < 100000)

def part2(s):
    max_size = 70000000
    size_needed = 30000000

    total, sizes = size(parse(s.split("$ ")), "")

    free = max_size - total

    return min(s for s in sizes.values() if free + s > size_needed)