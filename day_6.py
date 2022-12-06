import time
from collections import Counter

from aocd.models import Puzzle


def find_first_marker(data):
    counter = Counter()
    for i in range(len(data)-4):
        test_marker = data[i:i+4]
        counter.clear()
        counter.update(test_marker)
        if len(counter) == 4:
            return i+4

def find_message_marker(data):
    counter = Counter()
    for i in range(len(data)-14):
        test_marker = data[i:i+14]
        counter.clear()
        counter.update(test_marker)
        if len(counter) == 14:
            return i+14


def parse(puzzle_input: str) -> list:
    return puzzle_input.split('\n')


def solve_part_1(data: str) -> int:
    return find_first_marker(data)


def solve_part_2(data: str) -> int:
    return find_message_marker(data)


if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=6)
    puzzle_input = puzzle.input_data

    tic = time.perf_counter()
    part_1_answer = solve_part_1(puzzle_input)
    toc = time.perf_counter()
    print(f"Part 1 answer = {part_1_answer}")
    print(f"took {(toc-tic)*1000:0.1f} msec")

    tic = time.perf_counter()
    part_2_answer = solve_part_2(puzzle_input)
    toc = time.perf_counter()
    print(f"Part 2 answer = {part_2_answer}")
    print(f"took {(toc-tic)*1000:0.1f} msec")
