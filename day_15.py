from typing import NamedTuple

import parse


class Coord(NamedTuple):
    x: int
    y: int


class InputLine(NamedTuple):
    sensor: Coord
    beacon: Coord


def parse_input_line(line: str) -> NamedTuple:
    result = parse.search("Sensor at x={x_s:d}, y={y_s:d}: closest beacon is at x={x_b:d}, y={y_b:d}", line)
    sensor = Coord(result.named["x_s"], result.named["y_s"])
    beacon = Coord(result.named["x_b"], result.named["y_b"])
    return InputLine(sensor, beacon)


class BeaconExclusionZone:
    def __init__(self, sensor: NamedTuple, beacon: NamedTuple):
        self.sensor = sensor
        self.beacon = beacon
        self.rl_distance = rl_dist(self.sensor, self.beacon)

    def x_width(self, y: int) -> int:
        y_diff = abs(self.sensor.y - y)
        if y_diff > self.rl_distance:
            return 0

        return (self.rl_distance * 2) + 1 - (2 * y_diff)


def rl_dist(sensor: NamedTuple, beacon: NamedTuple) -> int:
    xs, ys = sensor
    xb, yb = beacon
    return abs(sensor.y - beacon.y) + abs(sensor.x - beacon.x)
