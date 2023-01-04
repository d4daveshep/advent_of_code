import time
from collections import Counter

from aocd.models import Puzzle
from typing import NamedTuple

import parse


class NoOverlap(Exception):
    pass


class Range:
    def __init__(self, start:int, end:int):
        self.start = start
        self.end = end
        if self.end < self.start:
            self.start, self.end = self.end, self.start

    def __repr__(self):
        return f"Range({self.start},{self.end})"

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __hash__(self):
        return hash((self.start, self.end))

    def __add__(self, other):
        if not self.overlap(other):
            raise NoOverlap
        else:
            return Range(min(self.start, other.start), max(self.end, other.end))

    def overlap(self, other) -> bool:
        if (self.start <= other.start and other.start <= self.end) or (self.start <= other.end and other.end <= self.end) or(self.start >= other.start and self.end <= other.end):
            return True
        else:
            return False


class RangeSet():
    ranges = []

    def __repr__(self):
        return f"RangeSet({[repr(r) for r in self.ranges]})"


    def add_range(self, range):
        self.ranges.append(range)
        self.__condense()

    def __len__(self):
        return len(self.ranges)

    def min(self):
        return min([r.start for r in self.ranges])

    def max(self):
        return max([r.end for r in self.ranges])

    def __condense(self):
        # for r in self.ranges:

        pass


class Coord(NamedTuple):
    x: int
    y: int


class InputLine(NamedTuple):
    sensor: Coord
    beacon: Coord


class Beacons:
    b_dict = {}

    def add_beacon(self, b: Coord):
        if b.y not in self.b_dict:
            self.b_dict[b.y] = set()
        self.b_dict[b.y].add(b.x)

    def get_beacon_x_set(self, y: int) -> set:
        if y not in self.b_dict:
            return set()
        else:
            return self.b_dict[y]


def tuning_frequency(beacon: Coord) -> int:
    return beacon.x * 4000000 + beacon.y


def parse_input_line(line: str) -> InputLine:
    result = parse.search("Sensor at x={x_s:d}, y={y_s:d}: closest beacon is at x={x_b:d}, y={y_b:d}", line)
    sensor = Coord(result.named["x_s"], result.named["y_s"])
    beacon = Coord(result.named["x_b"], result.named["y_b"])
    return InputLine(sensor, beacon)


class BeaconExclusionZone:
    def __init__(self, sensor: Coord, beacon: Coord):
        self.sensor = sensor
        self.beacon = beacon
        self.rl_distance = rl_dist(self.sensor, self.beacon)

    def x_width(self, y: int) -> int:
        y_diff = abs(self.sensor.y - y)
        if y_diff > self.rl_distance:
            return 0

        return (self.rl_distance * 2) + 1 - (2 * y_diff)

    def x_set(self, y: int) -> set:
        y_diff = abs(self.sensor.y - y)
        if y_diff > self.rl_distance:
            return set()

        x_min, x_max = self.x_min_max(y)
        x_set = {x for x in range(x_min, x_max + 1)}
        return x_set

    def x_min_max(self, y:int) -> tuple:
        y_diff = abs(self.sensor.y - y)
        if y_diff > self.rl_distance:
            return None

        x_min = self.sensor.x - (self.rl_distance - y_diff)
        x_max = self.sensor.x + (self.rl_distance - y_diff)
        return x_min, x_max



def rl_dist(sensor: Coord, beacon: Coord) -> int:
    xs, ys = sensor
    xb, yb = beacon
    return abs(sensor.y - beacon.y) + abs(sensor.x - beacon.x)



def parse_data(puzzle_input: str) -> list:
    return puzzle_input.split('\n')


def solve_part_1(data: list) -> int:
    all_x = set()
    beacons = Beacons()
    for input_line in data:
        # print(f"parsing line...{input_line}")
        line = parse_input_line(input_line.strip())
        beacons.add_beacon(line.beacon)
        bxz = BeaconExclusionZone(line.sensor, line.beacon)
        all_x.update(bxz.x_set(2000000))
        all_x.difference_update(beacons.get_beacon_x_set(2000000))

    return len(all_x)


def solve_part_2(data: list) -> int:
    all_x = set()
    beacons = Beacons()
    for input_line in data:
        # print(f"parsing line...{input_line}")
        line = parse_input_line(input_line.strip())
        beacons.add_beacon(line.beacon)
        bxz = BeaconExclusionZone(line.sensor, line.beacon)
        all_x.update(bxz.x_set(2000000))
        # all_x.difference_update(beacons.get_beacon_x_set(2000000))



if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=15)
    puzzle_input = puzzle.input_data
    data = parse_data(puzzle_input)

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
