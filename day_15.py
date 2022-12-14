import time
from typing import NamedTuple

import parse
from aocd.models import Puzzle


class NoOverlap(Exception):
    pass


class Range:
    def __init__(self, start: int, end: int):
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
        if (self.start <= other.start and other.start - 1 <= self.end) or (
                self.start - 1 <= other.end and other.end <= self.end) or (
                self.start >= other.start and self.end <= other.end):
            return True
        else:
            return False


def condense_ranges(ranges: list) -> list:
    if len(ranges) < 2:
        return ranges
    i = 0
    while i < len(ranges) - 1:
        r1 = ranges[i]
        r2 = ranges[i + 1]
        if r1.overlap(r2):
            ranges[i] = r1 + r2
            del ranges[i + 1]
        i += 1
    return ranges


class RangeSet():
    ranges = []

    def __repr__(self):
        return f"RangeSet({[repr(r) for r in self.ranges]})"

    # def add_range(self, range):
    #     self.ranges.append(range)
    #     self.ranges.sort(key=lambda r: r.start)

    def __len__(self):
        return len(self.ranges)

    def min(self):
        return min([r.start for r in self.ranges])

    def max(self):
        return max([r.end for r in self.ranges])

    def add_range(self, new_range: Range):
        new_RS = []
        added = False
        for r in self.ranges:
            if r.overlap(new_range):
                new_RS.append(r + new_range)
                added = True
            else:
                new_RS.append(r)
        if not added:
            new_RS.append(new_range)
        new_RS.sort(key=lambda r: r.start)

        self.ranges = new_RS
        self.condense()

    def condense(self):
        self.ranges = condense_ranges(self.ranges)

    def gaps(self) -> list:
        gaps = []
        for i in range(len(self.ranges) - 1):
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

    def __repr__(self):
        return f"BeaconExclusionZone(sensor={self.sensor}, beacon={self.beacon})"

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

    def x_min_max(self, y: int) -> tuple:
        y_diff = abs(self.sensor.y - y)
        if y_diff > self.rl_distance:
            return None

        x_min = max(0, self.sensor.x - (self.rl_distance - y_diff))
        x_max = min(4000000, self.sensor.x + (self.rl_distance - y_diff))
        return x_min, x_max

    def y_min_max(self) -> tuple:
        y_min = max(0, self.sensor.y - self.rl_distance)
        y_max = min(4000000, self.sensor.y + self.rl_distance)
        return y_min, y_max


def rl_dist(sensor: Coord, beacon: Coord) -> int:
    xs, ys = sensor
    xb, yb = beacon
    return abs(sensor.y - beacon.y) + abs(sensor.x - beacon.x)


def build_bxzs(data: list) -> list:
    bxzs = []
    for input_line in data:
        line = parse_input_line(input_line)
        bxzs.append(BeaconExclusionZone(line.sensor, line.beacon))
    print(f"created {len(bxzs)} BeaconExclusionZones")
    return bxzs


def get_range_set(bxzs: list, y: int) -> RangeSet:
    range_set = RangeSet()
    for bxz in bxzs:
        x_width = bxz.x_width(y)
        x_tup = bxz.x_min_max(y)
        if x_tup is not None:
            range_set.add_range(Range(x_tup[0], x_tup[1]))
    range_set.condense()
    return range_set


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
    # build list of beacon exclusion zones
    bxzs = build_bxzs(data)

    range_sets = {}

    for y in range(0, 4000001):
        # for y in range(2900000, 2910000):
        # print(f"processing y = {y}")
        range_set = get_range_set(bxzs, y)
        range_sets[y] = range_set

    # find range sets with len of 2 (i.e. a single gap)
    range_gaps = {k: v for k, v in range_sets.items() if len(v) > 1}
    # print(f"lines with gaps... {range_gaps}")

    for y, range_set in range_gaps.items():
        x = range_set.ranges[0].end + 1
        beacon = Coord(x, y)
        print(f"tuning frequency={tuning_frequency(beacon)}")


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
