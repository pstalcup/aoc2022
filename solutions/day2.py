# A, X, 1 = Rock
# B, Y, 2 = Paper
# C, Z, 3 = Scissors

def part1(s):
    wins = ["A Y", "B Z", "C X"]
    ties = ["A X", "B Y", "C Z"]

    return s.count("X") + 2 * s.count("Y") + 3 * s.count("Z") + 6 * sum(s.count(r) for r in wins) + 3 * sum(s.count(r) for r in ties)

def part2(s):
    lookup = dict(
        Z=dict(A=2, B=3, C=1),
        Y=dict(A=1, B=2, C=3),
        X=dict(A=3, B=1, C=2)
    )

    return 3 * s.count("Y") + 6 * s.count("Z") + sum(lookup[r[2]][r[0]] for r in s.split("\n") if r != "")