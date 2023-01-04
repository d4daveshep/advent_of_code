from typing import NamedTuple

import parse
import pytest

from day_15 import rl_dist, BeaconExclusionZone, Coord, parse_input_line, Beacons, InputLine, tuning_frequency


@pytest.fixture()
def test_data():
    with open("./day_15_test_data.txt") as data_file:
        data = data_file.readlines()
    return data


@pytest.fixture()
def line_8_7() -> InputLine:
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
    sensor = Coord(x=8, y=7)
    beacon = Coord(x=2, y=10)
    assert rl_dist(sensor, beacon) == 9


def test_x_width_at_y(line_8_7):
    bxz = BeaconExclusionZone(line_8_7.sensor, line_8_7.beacon)
    assert bxz.x_width(7) == 19
    assert bxz.x_width(6) == bxz.x_width(8) == 17
    assert bxz.x_width(-2) == bxz.x_width(16) == 1
    assert bxz.x_width(-3) == bxz.x_width(17) == 0


def test_x_set_at_y(line_8_7):
    bxz = BeaconExclusionZone(line_8_7.sensor, line_8_7.beacon)
    assert bxz.x_set(7) == {x for x in range(-1, 18)}
    assert bxz.x_set(6) == bxz.x_set(8) == {x for x in range(0, 17)}
    assert bxz.x_set(-2) == bxz.x_set(16) == {8}
    assert bxz.x_set(-3) == bxz.x_set(17) == set()


def test_all_x_sets(test_data):
    all_x = set()
    beacons = Beacons()
    for input_line in test_data:
        line = parse_input_line(input_line)
        beacons.add_beacon(line.beacon)
        bxz = BeaconExclusionZone(line.sensor, line.beacon)
        all_x.update(bxz.x_set(10))
        all_x.difference_update(beacons.get_beacon_x_set(10))

    assert len(all_x) == 26

def test_tuning_frequency():
    beacon = Coord(x=14,y=11)
    assert tuning_frequency(beacon) == 56000011
