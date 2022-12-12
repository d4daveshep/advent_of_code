import time
from enum import Enum
from typing import NamedTuple

from aocd.models import Puzzle


class Move(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


move_map = {"U": Move.UP, "D": Move.DOWN, "L": Move.LEFT, "R": Move.RIGHT}


class Vector(NamedTuple):
    x: int
    y: int


class Point:
    def __init__(self, x: int, y: int):
        self.__positions = {}
        self.x = x
        self.y = y
        self.store_position()

    def __repr__(self):
        return f"Point({self.x},{self.y})"

    def __eq__(self, other) -> bool:
        assert isinstance(other, Point)
        return self.x == other.x and self.y == other.y

    def move(self, direction: Move, store=True):
        if direction == Move.UP:
            self.y += 1
        elif direction == Move.DOWN:
            self.y -= 1
        elif direction == Move.LEFT:
            self.x -= 1
        elif direction == Move.RIGHT:
            self.x += 1

        if store:
            self.store_position()
        return self

    def gap_to(self, other) -> Vector:
        assert isinstance(other, Point)
        return Vector(other.x - self.x, other.y - self.y)

    def is_adjacent_to(self, other) -> bool:
        assert isinstance(other, Point)
        gap = other.gap_to(self)
        if abs(gap.x) > 1 or abs(gap.y) > 1:
            return False
        else:
            return True

    def store_position(self):
        self.__positions[self.__repr__()] = True

    def clear_positions(self):
        self.__positions.clear()

    def count_unique_positions(self) -> int:
        return len(self.__positions)


class Rope:
    def __init__(self, head: Point = Point(0, 0), tail: Point = Point(0, 0), knots: int = 2):
        self.num_knots = knots
        self.knot = []
        for _ in range(self.num_knots):
            self.knot.append(Point(0, 0))
        if head:
            self.knot[0] = head
        if tail:
            self.knot[-1] = tail

    @property
    def head(self):
        return self.knot[0]

    @property
    def tail(self):
        return self.knot[-1]

    def move_head(self, direction: Move):
        self.head.move(direction)
        for k in range(self.num_knots - 1):
            if self.knot[k + 1].is_adjacent_to(self.knot[k]):
                return
            else:
                self.close_gap(self.knot[k], self.knot[k + 1])

    def gap_tail_to_head(self) -> Vector:
        return self.tail.gap_to(self.head)

    def tail_is_adjacent_to_head(self) -> bool:
        return self.tail.is_adjacent_to(self.head)

    def close_gap(self, leader: Point, follower: Point):
        gap = follower.gap_to(leader)
        # gap = self.gap_tail_to_head()
        if gap == Vector(2, 0):
            follower.move(Move.RIGHT)
        elif gap == Vector(-2, 0):
            follower.move(Move.LEFT)
        elif gap == Vector(0, 2):
            follower.move(Move.UP)
        elif gap == Vector(0, -2):
            follower.move(Move.DOWN)
        elif gap == Vector(1, 2) or gap == Vector(2, 1) or gap == Vector(2, 2):
            follower.move(Move.UP, store=False)
            follower.move(Move.RIGHT)
        elif gap == Vector(1, -2) or gap == Vector(2, -1) or gap == Vector(2, -2):
            follower.move(Move.DOWN, store=False)
            follower.move(Move.RIGHT)
        elif gap == Vector(-1, -2) or gap == Vector(-2, -1) or gap == Vector(-2, -2):
            follower.move(Move.DOWN, store=False)
            follower.move(Move.LEFT)
        elif gap == Vector(-1, 2) or gap == Vector(-2, 1) or gap == Vector(-2, 2):
            follower.move(Move.UP, store=False)
            follower.move(Move.LEFT)
        else:
            raise Exception(f"Gap too big: {gap}")

    def do_multiple_moves(self, dir_num: str):
        dir, num = dir_num.split()
        for _ in range(int(num)):
            self.move_head(move_map[dir])


def parse(puzzle_input: str) -> list:
    return puzzle_input.split('\n')


def solve_part_1(data: list) -> int:
    rope = Rope(head=Point(0, 0), tail=Point(0, 0))
    for line in data:
        line = line.strip()
        rope.do_multiple_moves(line)
    return rope.tail.count_unique_positions()


def solve_part_2(data: list) -> int:
    rope = Rope(knots=10)
    for line in data:
        line = line.strip()
        rope.do_multiple_moves(line)
    return rope.tail.count_unique_positions()



if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=9)
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
