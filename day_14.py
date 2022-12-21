# alternate solution for Day 12 using my own Graph structure
import time
from collections import deque
from functools import cmp_to_key
from itertools import zip_longest
from operator import itemgetter

from aocd.models import Puzzle

AIR = "."
ROCK = "#"
SAND = "o"

class Cave:
    def __init__(self):
        self.space = {}

    def __getitem__(self, y) -> list:
        if y not in self.space:
            self.space[y] = [AIR for i in range(30)]
        return self.space[y]

    def add_walls(self, tuples_list:list):
        for row in tuples_list:
            for i in range(len(row)-1):
                start = row[i]
                end = row[i+1]
                self.add_wall(start, end)

    def add_wall(self, start:tuple, end:tuple):
        x1,y1 = start
        x2,y2 = end
        x_dir = x2 - x1 // abs(x2-x1)
        y_dir = y2 - y1 // abs(y2-y1)
        for x in range(x1,x2+1,x_dir):




def parse_data_to_tuples_list(test_data):
    return [[eval(t) for t in line.split(" -> ")] for line in test_data]


def find_dimensions(tuples_list):
    min_x = min_y = None
    max_x = max_y = None
    for line in tuples_list:
        min_x = min(line, key=itemgetter(0))
        min_y = min(line, key=itemgetter(1))
        max_x = max(line, key=itemgetter(0))
        max_y = max(line, key=itemgetter(1))

    return ((min_x[0], min_y[1]), (max_x[0], max_y[1]))



def parse(puzzle_input: str) -> list:
    return puzzle_input.split('\n')


def solve_part_1(data: list) -> int:
    tuples_list = parse_data_to_tuples_list(data)
    min, max = find_dimensions(tuples_list)
    print(f"min={min}, max={max}")
    return 0

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
