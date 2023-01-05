import parse
import pytest

from day_15 import rl_dist, BeaconExclusionZone, Coord, parse_input_line, Beacons, InputLine, tuning_frequency, Range, \
    NoOverlap, RangeSet, condense_ranges


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

def test_x_min_max(line_8_7):
    bxz = BeaconExclusionZone(line_8_7.sensor, line_8_7.beacon)
    assert bxz.x_min_max(7) == (-1, 17)
    assert bxz.x_min_max(6) == (0,16)
    assert bxz.x_min_max(-2) == (8,8)
    assert bxz.x_min_max(-3) is None


def test_part_2(test_data):
    # build list of beacon exclusion zones
    bxzs = []
    for input_line in test_data:
        line = parse_input_line(input_line)
        bxzs.append(BeaconExclusionZone(line.sensor, line.beacon))

    range_sets = {}

    for y in range(0, 21):

        range_set = RangeSet()
        range_sets[y] = range_set

        for bxz in bxzs:
            x_tup = bxz.x_min_max(y)
            if x_tup is not None:
                range_set.add_range(Range(x_tup[0], x_tup[1]))
        range_set.condense()

    pass
    # find range sets with len of 2 (i.e. a single gap)
    # calculate the tuning frequency of this y value




def test_tuning_frequency():
    beacon = Coord(x=14, y=11)
    assert tuning_frequency(beacon) == 56000011


def test_range_overlap():
    r1 = Range(2, 4)
    r2 = Range(3, 5)
    r3 = Range(6, 10)
    r4 = Range(7, 9)

    assert r1.overlap(r2)
    assert r2.overlap(r1)
    assert not r1.overlap(r3)
    assert not r3.overlap(r1)
    assert r3.overlap(r4)
    assert r4.overlap(r3)


def test_range_start_end_reversed():
    r1 = Range(4, 2)
    r2 = Range(3, 5)
    r3 = Range(10, 6)
    r4 = Range(7, 9)

    assert r1.overlap(r2)
    assert r2.overlap(r1)
    assert not r1.overlap(r3)
    assert not r3.overlap(r1)
    assert r3.overlap(r4)
    assert r4.overlap(r3)

    r5 = Range(12,14)
    r6 = Range(-8,12)
    assert r5.overlap(r6)
    assert r6.overlap(r5)


def test_range_equality():
    r1 = Range(2, 4)
    r2 = Range(2, 4)
    r3 = Range(4, 2)
    assert r1 == r2
    assert r2 == r3
    r4 = Range(3, 4)
    assert r3 != r4


def test_adding_overlapping_ranges():
    r1 = Range(2, 4)
    r2 = Range(3, 5)
    r3 = Range(6, 10)
    r4 = Range(7, 9)

    assert r1 + r2 == Range(2, 5)
    assert r3 + r4 == r3
    with pytest.raises(NoOverlap):
        r0 = r1 + r3




def test_rangeset_len_min_max():
    range_set = RangeSet()
    range_set.add_range(Range(6,10))
    assert len(range_set) == 1
    assert range_set.min() == 6
    assert range_set.max() == 10

    range_set.add_range(Range(2,4))
    assert len(range_set) == 2
    assert range_set.min() == 2
    assert range_set.max() == 10

def test_rangeset_sorting():
    range_set = RangeSet()
    r610 = Range(6,10)
    r24 = Range(2,4)
    r55 = Range(5,5)

    range_set.add_range(r610)
    range_set.add_range(r24)

    assert range_set.ranges[0] == r24
    assert range_set.ranges[1] == r610

    range_set.add_range(r55)

    assert range_set.ranges[0] == r24
    assert range_set.ranges[1] == r55
    assert range_set.ranges[2] == r610

def test_range_condensing_1():
    range_set = RangeSet()
    r610 = Range(6,10)
    r24 = Range(2,4)
    r35 = Range(3,5)
    r79 = Range(7,9)

    range_set.add_range(r24)
    range_set.add_range(r610)
    range_set.add_range(r35)

    assert len(range_set) == 2
    assert range_set.ranges[0] == Range(2,5)
    assert range_set.ranges[1] == r610

    range_set.add_range(r79)

    assert len(range_set) == 2
    assert range_set.ranges[0] == Range(2,5)
    assert range_set.ranges[1] == r610

def test_range_condensing_2():
    range_set = RangeSet()

    range_set.add_range(Range(1,10))
    range_set.add_range(Range(1,2))
    range_set.add_range(Range(3,4))
    range_set.add_range(Range(5,6))
    range_set.add_range(Range(7,8))
    range_set.add_range(Range(9,10))

    assert len(range_set) == 1
    assert range_set.min() == 1
    assert range_set.max() == 10

def test_range_adding_condension_3():
    range_set = RangeSet()
    range_set.add_range(Range(12,14))
    range_set.add_range(Range(6,10))
    range_set.add_range(Range(-8,12))

    assert len(range_set) == 1
    assert range_set.min() == -8
    assert range_set.max() == 14

def test_condense_ranges():
    range_set = RangeSet()
    range_set.add_range(Range(12,14))

    range_set.condense()

    range_set.add_range(Range(6,10))
    range_set.condense()

    range_set.add_range(Range(-8,12))
    range_set.condense()

    assert len(range_set) == 1
    assert range_set.min() == -8
    assert range_set.max() == 14






