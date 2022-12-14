example = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""
def sign(a):
    return 0 if a == 0 else (-1 if a < 0 else 1)


def shared(s):
    board = {}
    floor = 0
    for regoliths in s.split("\n")[:-1]:
        path = [[int(n) for n in p.split(",")] for p in regoliths.split("->")]
        for i in range(len(path) - 1):
            sx, sy = path[i]
            ex, ey = path[i + 1]
            dx, dy = ex - sx, ey - sy
            floor = max(floor, ey, sy)

            for i in range(max(abs(dx), abs(dy))):
                board[(sx + sign(dx) * i, sy + sign(dy) * i)] = 0
        board[(path[-1][0], path[-1][1])] = 0

    return board, floor

def part1(s):
    board, floor = shared(s) 

    start = (500, 0)
    prev = (0, 0)
    cur = start

    while prev != cur:
        if cur[1] > floor and prev == cur:
            break
        elif cur[1] > floor:
            prev = cur
            cur = start

        down = (cur[0], cur[1] + 1)
        left = (cur[0] - 1, cur[1] + 1)
        right = (cur[0] + 1, cur[1] + 1)

        if all(p in board for p in [down, left, right]):
            board[cur] = 1
            cur = start
        else:
            cur = [p for p in [down, left, right] if p not in board][0]

    return sum(board.values())

def part2(s):
    board, floor = shared(s) 

    start = (500, 0)
    prev = (0, 0)
    cur = start

    while True:
        if cur[1] + 1 == floor + 2:
            board[cur] = 1
            cur = start

        down = (cur[0], cur[1] + 1)
        left = (cur[0] - 1, cur[1] + 1)
        right = (cur[0] + 1, cur[1] + 1)

        if all(p in board for p in [down, left, right]):
            board[cur] = 1
            if cur == start:
                break
            cur = start
        else:
            cur = [p for p in [down, left, right] if p not in board][0]
    return sum(board.values())