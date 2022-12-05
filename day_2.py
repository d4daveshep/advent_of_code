# day_1.py
from collections import Counter

from aocd.models import Puzzle


def parse(puzzle_input: str) -> list:
    """Parse input."""
    data = puzzle_input.split('\n')
    return data


def solve_part_1(data: list) -> int:
    counter = Counter(data)

    scoring = {"A X": [1, 3],
               "A Y": [2, 6],
               "A Z": [3, 0],
               "B X": [1, 0],
               "B Y": [2, 3],
               "B Z": [3, 6],
               "C X": [1, 6],
               "C Y": [2, 0],
               "C Z": [3, 3]}

    total_score = 0
    for result, count in counter.items():
        score = scoring[result]
        total_score += sum(score) * count

    return total_score


def solve_part_2(data: list) -> int:
    counter = Counter(data)

    scoring = {"A X": [3, 0],
               "A Y": [1, 3],
               "A Z": [2, 6],
               "B X": [1, 0],
               "B Y": [2, 3],
               "B Z": [3, 6],
               "C X": [2, 0],
               "C Y": [3, 3],
               "C Z": [1, 6]}

    total_score = 0
    for result, count in counter.items():
        score = scoring[result]
        total_score += sum(score) * count

    return total_score


if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=2)
    puzzle_input = puzzle.input_data

    data = parse(puzzle_input)

    solution_1 = solve_part_1(data)
    print(f"Part 1 solution = {solution_1}")

    solution_2 = solve_part_2(data)
    print(f"Part 2 solution = {solution_2}")
