def sign(a):
    return 0 if a == 0 else (-1 if a < 0 else 1)

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, d):
        self.x, self.y = self.x + dict(U=-1,D=1).get(d, 0), self.y + dict(L=-1,R=1).get(d, 0)

    def follow(self, b):
        if abs(b.x - self.x) > 1 or abs(b.y - self.y) > 1:
            self.x, self.y = self.x + sign(b.x - self.x), self.y + sign(b.y - self.y)

def part1(s):
    moves = [(l[0], int(l[2:])) for l in s.split("\n") if len(l) > 0]
    h, t = Pos(0, 0), Pos(0, 0)
    visited = dict()

    for d, m in moves:
        for i in range(m):
            h.move(d)
            t.follow(h)

            visited[(t.x, t.y)] = 1

    return sum(visited.values())

def part2(s):
    moves = [(l[0], int(l[2:])) for l in s.split("\n") if len(l) > 0]
    k = [Pos(0, 0) for i in range(10)]
    visited = dict()

    for d, m in moves:
        for i in range(m):
            k[0].move(d)
            [k[i + 1].follow(k[i]) for i in range(9)]
            visited[(k[-1].x, k[-1].y)] = 1
    
    return sum(visited.values())