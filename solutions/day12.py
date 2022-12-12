import string
from itertools import chain

ex = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""

class Pos:
    def __init__(self, r, c):
        self.r = r
        self.c = c 
    
    def __hash__(self):
        return hash((self.r, self.c))
    
    def __eq__(self, b):
        return hash(self) == hash(b)
    
    def valid(self):
        return self.r < self.maxr and self.r >= 0 and self.c < self.maxc and self.c >= 0

    def adj(self, visited):
        possible = chain.from_iterable([Pos(self.r + d, self.c), Pos(self.r, self.c + d)] for d in [1, -1])
        return [p for p in possible if p.valid() and p not in visited and self.height[self] - self.height[p] <= 1]

def shared(s):
    lines = s.split("\n")[:-1]
    Pos.maxr, Pos.maxc = len(lines), len(lines[0]) # assume a square input
    Pos.height = {Pos(r, c):string.ascii_lowercase.index(lines[r][c].replace("S","a").replace("E","z")) for r in range(Pos.maxr) for c in range(Pos.maxc)}

    sr = ["S" in l for l in lines].index(True)
    sc = lines[sr].index("S")

    er = ["E" in l for l in lines].index(True)
    ec = lines[er].index("E")

    start = Pos(sr, sc)
    end = Pos(er, ec)

    dist = {end: 0}
    source = {}
    visited = set()

    while len(visited) < Pos.maxr * Pos.maxc:
        options = sorted((k for k in dist.keys() if k not in visited), key=lambda p: dist[p])
        if len(options) == 0:
            break
        current = options[0]
        visited.add(current)
        for adj in current.adj(visited):
            if adj not in dist or dist[adj] < dist[current] + 1:
                dist[adj] = dist[current] + 1
                source[adj] = current
    
    return start, end, dist

def part1(s):
    start, end, dist = shared(s)
    return dist[start]

def part2(s):
    start, end, dist = shared(s)
    closest = sorted((p for p, h in Pos.height.items() if h == 0), key=lambda x:dist.get(x, Pos.maxr * Pos.maxc))[0]
    return dist[closest]