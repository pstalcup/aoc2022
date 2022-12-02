import sys, re, os
import solutions

if __name__ == "__main__":
    day_regex = re.compile("day\d")
    days = [p for p in sys.argv if day_regex.match(p)]

    parts = ["part1", "part2"]

    for day in days:
        print("----")
        print(day)
        with open(os.path.join(os.path.dirname(__file__), "inputs", f"{day}.txt")) as f:
            s = f.read()

        __import__(f"solutions.{day}")
        mod = getattr(solutions, day)
        for part in parts:
            if hasattr(mod, part):
                print(f"{part}: {getattr(mod, part)(s)}")