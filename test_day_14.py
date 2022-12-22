import pytest

from day_14 import parse_data_to_tuples_list, find_dimensions, Cave, AIR, ROCK, SAND


@pytest.fixture()
def test_data():
    with open("./day_14_test_data.txt") as data_file:
        data = data_file.readlines()
    return data


@pytest.fixture()
def tuples_list(test_data):
    return parse_data_to_tuples_list(test_data)


def test_parse_data(test_data):
    tuples_list = parse_data_to_tuples_list(test_data)
    assert len(tuples_list) == 2
    assert [(498, 4), (498, 6), (496, 6)] in tuples_list


def test_find_dimensions(tuples_list):
    min, max = find_dimensions(tuples_list)
    assert min == (494, 4)
    assert max == (503, 9)


def test_create_cave():
    cave = Cave()
    assert cave[500][5] == AIR
    cave[500][5] = ROCK
    assert cave[500][5] == ROCK


def test_add_cave_walls(tuples_list):
    cave = Cave()
    cave.add_walls(tuples_list)
    assert cave[498][4] == ROCK
    assert cave[498][5] == ROCK
    assert cave[498][6] == ROCK
    assert cave[497][6] == ROCK
    assert cave[496][6] == ROCK

    cave.print_shape()


@pytest.fixture()
def cave(tuples_list):
    cave = Cave()
    cave.add_walls(tuples_list)
    return cave


def test_top_solid(cave):
    assert cave.top_solid(498) == 4
    assert cave.top_solid(500) == 9
    assert cave.top_solid(502) == 4
    assert cave.top_solid(1) is None


def test_cant_overwrite_rock(cave):
    assert cave[498][4] == ROCK
    with pytest.raises(Exception):
        cave.add_material(498, 4, SAND)

    with pytest.raises(Exception):
        cave.add_material(498, 4, AIR)


def test_add_sand(cave):
    cave.print_shape()

    cave.add_sand()
    # cave.print_shape()
    assert cave[500][8] == SAND
    assert cave.top_solid(500) == 8

    cave.add_sand()
    # cave.print_shape()
    assert cave[499][8] == SAND

    cave.add_sand()
    # cave.print_shape()
    assert cave[501][8] == SAND

    cave.add_sand()
    # cave.print_shape()
    assert cave[500][7] == SAND

    cave.add_sand()
    # cave.print_shape()
    assert cave[498][8] == SAND

    cave.add_sand()
    # cave.print_shape()
    assert cave[499][7] == SAND

    cave.add_sand()
    # cave.print_shape()
    assert cave[501][7] == SAND

    cave.add_sand()
    # cave.print_shape()
    assert cave[500][6] == SAND

    cave.add_sand()
    # cave.print_shape()
    assert cave[497][8] == SAND

    cave.add_sand()
    # cave.print_shape()
    assert cave[498][7] == SAND

    cave.add_sand()
    # cave.print_shape()
    assert cave[499][6] == SAND

    cave.add_sand()
    # cave.print_shape()
    assert cave[501][6] == SAND

    for _ in range(10):
        cave.add_sand()
    # cave.print_shape()

    cave.add_sand()
    # cave.print_shape()
    assert cave[497][5] == SAND

    cave.add_sand()
    cave.print_shape()
    assert cave[495][8] == SAND

    assert cave.count_sand() == 24

def test_add_sand_until_full(cave):
    cave.fill_with_sand(col=500)
    assert cave.count_sand() == 24


