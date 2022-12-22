from typing import NamedTuple

import parse
import pytest

from day_15 import rl_dist, BeaconExclusionZone, Coord, parse_input_line


@pytest.fixture()
def test_data():
    with open("./day_15_test_data.txt") as data_file:
        data = data_file.readlines()
    return data


@pytest.fixture()
def line_8_7() -> NamedTuple:
    return parse_input_line("Sensor at x=8, y=7: closest beacon is at x=2, y=10")


def test_parse_input_line():
    line = "Sensor at x=9, y=16: closest beacon is at x=10, y=16"
    result = parse.search("Sensor at x={x_s:d}, y={y_s:d}: closest beacon is at x={x_b:d}, y={y_b:d}", line)
    assert result.named["x_s"] == 9
    assert result.named["y_s"] == 16
    assert result.named["x_b"] == 10
    assert result.named["y_b"] == 16


def test_build_function():
    line = "Sensor at x=8, y=7: closest beacon is at x=2, y=10"


def test_rectilinear_distance():
    sensor = Coord(x=9, y=16)
    beacon = Coord(x=10, y=16)
    assert rl_dist(sensor, beacon) == 9


def test_x_width_at_y(line_8_7):
    bxz = BeaconExclusionZone(line_8_7.sensor, line_8_7.beacon)
    assert bxz.x_width(7) == 19
    assert bxz.x_width(6) == bxz.x_width(8) == 17
    assert bxz.x_width(-2) == bxz.x_width(16) == 1
    assert bxz.x_width(-3) == bxz.x_width(17) == 0


def test_x_set_at_y(line_8_7):
    pass
