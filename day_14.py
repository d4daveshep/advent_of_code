# alternate solution for Day 12 using my own Graph structure
import time

from aocd.models import Puzzle

AIR = "."
ROCK = "#"
SAND = "o"


class Cave:
    def __init__(self):
        self.__space = {}

    def __getitem__(self, y) -> list:
        if y not in self.__space:
            self.__space[y] = [AIR for i in range(160)]
        return self.__space[y]

    def add_walls(self, tuples_list: list):
        for row in tuples_list:
            for i in range(len(row) - 1):
                start = row[i]
                end = row[i + 1]
                self.add_wall(start, end)

    def add_wall(self, start: tuple, end: tuple):
        x1, y1 = start
        x2, y2 = end

        if x1 == x2:  # vertical
            for y in range(min([y1, y2]), max([y1, y2]) + 1):
                self.add_material(x1, y, ROCK)

        elif y1 == y2:  # horizontal
            for x in range(min([x1, x2]), max([x1, x2]) + 1):
                self.add_material(x, y1, ROCK)

    def add_material(self, x, y, material: str):
        # print(f"adding {x},{y}")
        if material is not ROCK and self[x][y] == ROCK:
            raise Exception(f"Can't add {material} over ROCK")
        self[x][y] = material

    def add_sand(self, col=500):
        top = self.top_solid(col)
        top_left = self.top_solid(col - 1)
        top_right = self.top_solid(col + 1)

        if top_left == top and top == top_right:
            # Sand at rest
            self.add_material(col, top - 1, SAND)

        elif top_left > top:
            self.add_material(col - 1, top_left - 1, SAND)

        elif top_right > top:
            self.add_material(col + 1, top_right - 1, SAND)

    def print_shape(self):
        print()
        for key in sorted(self.__space.keys()):
            print(f"{key}:", end="")
            for y in self[key]:
                print(f"{y}", end="")
            print()

    def top_solid(self, col: int) -> int:
        try:
            rock_index = self[col].index(ROCK)
        except ValueError:
            return None
        try:
            sand_index = self[col].index(SAND)
        except ValueError:
            return rock_index

        return min([rock_index, sand_index])


def parse_data_to_tuples_list(test_data):
    return [[eval(t) for t in line.split(" -> ")] for line in test_data]


def find_dimensions(tuples_list):
    min_x = min_y = 1000
    max_x = max_y = 0
    for line in tuples_list:
        for x, y in line:
            min_x = min([min_x, x])
            min_y = min([min_y, y])
            max_x = max([max_x, x])
            max_y = max([max_y, y])

    return ((min_x, min_y), (max_x, max_y))


def parse(puzzle_input: str) -> list:
    return puzzle_input.split('\n')


def solve_part_1(data: list) -> int:
    tuples_list = parse_data_to_tuples_list(data)
    min, max = find_dimensions(tuples_list)
    print(f"min={min}, max={max}")

    cave = Cave()
    cave.add_walls(tuples_list)
    cave.print_shape()

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
