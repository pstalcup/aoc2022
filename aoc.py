import sys, re, os
import solutions

def base():
    return os.path.dirname(__file__)

if __name__ == "__main__":
    day_regex = re.compile("day\d")
    days = [p for p in sys.argv if day_regex.match(p)]

    mode = "run"
    for m in sys.argv:
        if m == "solved":
            mode = "solved"

    parts = ["part1", "part2"]

    for day in days:
        print("----")
        print(day)

        if mode == "run":
            with open(os.path.join(base(), "inputs", f"{day}.txt")) as f:
                s = f.read()

            __import__(f"solutions.{day}")
            mod = getattr(solutions, day)
            for part in parts:
                if hasattr(mod, part):
                    print(f"{part}: {getattr(mod, part)(s)}")
        elif mode == "solved":
            progress_path = os.path.join(base(), "progress.txt")
            if(os.path.exists(progress_path)):
                with open(progress_path, "r") as f:
                    all_solved = list(set(f.read().split("\n")[:-1] + [day]))
            else:
                all_solved = [day]
            
            with open(progress_path, "w") as f:
                for s in sorted(all_solved, key=lambda x: int(x.replace("day", ""))):
                    f.write(f"{s}\n")
                