import sys, re, os
import solutions

def base():
    return os.path.dirname(__file__)

if __name__ == "__main__":
    progress_path = os.path.join(base(), "progress.txt")
    day_regex = re.compile("day\d")
    days = [p for p in sys.argv if day_regex.match(p)]

    mode = (["run"] + [x for x in ["run", "solved", "progress"] if x in sys.argv])[-1]

    if mode == "progress":
        if(os.path.exists(progress_path)):
            with(open(progress_path, "r")) as f:
                all_solved = f.read().split("\n")[:-1]
                for solved in all_solved:
                    print(solved)
        else:
            print("No solutions!")
    else:
        for day in days:
            print("----")
            print(day)

            if mode == "run":
                parts = ["part1", "part2"]
                with open(os.path.join(base(), "inputs", f"{day}.txt")) as f:
                    s = f.read()

                __import__(f"solutions.{day}")
                mod = getattr(solutions, day)
                for part in parts:
                    if hasattr(mod, part):
                        print(f"{part}: {getattr(mod, part)(s)}")
            elif mode == "solved":
                if(os.path.exists(progress_path)):
                    with open(progress_path, "r") as f:
                        all_solved = list(set(f.read().split("\n")[:-1] + [day]))
                else:
                    all_solved = [day]
                
                with open(progress_path, "w") as f:
                    for s in sorted(all_solved, key=lambda x: int(x.replace("day", ""))):
                        f.write(f"{s}\n")