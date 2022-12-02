# Advent of Code 2022

[Advent of Code](https://adventofcode.com/) is a programming challenge that is run annually. These are my soltuions to the 2022 competition.


## Running

To run:

```bash
python3 aoc.py dayN ... 
```

Where N is a number (1 based) representing the day of the puzzle.

`solutions/dayN.py` is expected to define functions `part1` and `part2`, each taking a string as an argument.

When called, these functions should return the solution for that days part 1 and part 2 respectively.


## Tracking Progress

To track progress:

```bash
python3 aoc.py solved dayN ... 
```

Where N is a number (1 based) representing the day of the puzzle. This will update the `progress.txt` file with all days that have solutions.
