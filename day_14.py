# alternate solution for Day 12 using my own Graph structure
import time
from collections import deque
from functools import cmp_to_key
from itertools import zip_longest

from aocd.models import Puzzle



def parse_data_to_tuples_list(test_data):
    return [[eval(t) for t in line.split(" -> ")] for line in test_data]



def parse(puzzle_input: str) -> list:
    return puzzle_input.split('\n')


def solve_part_1(data: list) -> int:
    pass

def solve_part_2(data: list) -> int:
    pass

if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=14)
    puzzle_input = puzzle.input_data
    data = parse(puzzle_input)

    tic = time.perf_counter()
    part_1_answer = solve_part_1(data)
    toc = time.perf_counter()
    print(f"Part 1 answer = {part_1_answer}")
    print(f"took {(toc - tic) * 1000:0.1f} msec")

    tic = time.perf_counter()
    part_2_answer = solve_part_2(data)
    toc = time.perf_counter()
    print(f"Part 2 answer = {part_2_answer}")
    print(f"took {(toc - tic) * 1000:0.1f} msec")
