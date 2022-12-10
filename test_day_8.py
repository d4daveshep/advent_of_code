import pandas as pd
import pytest

from day_8 import build_dataframe, convert_string_to_list_of_ints, calc_perimeter_length, north_visibility, \
    south_visibility, west_visibility, east_visibility, calc_visibility_of_internal_cells, calc_total_visible_cells, \
    calc_trees_visible_north, calc_trees_visible_south, calc_trees_visible_west, calc_trees_visible_east, \
    calc_scenic_score


@pytest.fixture()
def data() -> list:
    with open("./day_8_data.txt") as data_file:
        data = data_file.readlines()
    return data


@pytest.fixture()
def df(data):
    return build_dataframe(data)





def test_convert_string_to_list_of_ints():
    data_string = "30373"
    ints = convert_string_to_list_of_ints(data_string)
    assert len(ints) == len(data_string)
    for i in range(len(data_string)):
        assert ints[i] == int(data_string[i])



def test_load_dataframe(data):
    df = build_dataframe(data)
    assert df.shape == (5, 5)
    assert df[0][0] == 3
    assert df[1][1] == 5
    assert df[2][2] == 3
    assert df[3][3] == 4
    assert df[4][4] == 0




def test_edge_count(df):
    edge_count = calc_perimeter_length(df)
    assert edge_count == 16




def test_north_visibility_of_cell(df):
    assert north_visibility(df, (1, 1)) == True
    assert north_visibility(df, (2, 1)) == False


def test_south_visibilty_of_cell(df):
    assert south_visibility(df, (3, 2)) == True
    assert south_visibility(df, (2, 3)) == False


def test_west_visibility_of_cell(df):
    assert west_visibility(df, (2, 2)) == False
    assert west_visibility(df, (3, 2)) == True


def test_east_visibilty_of_cells(df):
    assert east_visibility(df, (2, 3)) == True
    assert east_visibility(df, (3, 2)) == False




def test_calc_visibility_of_internal_cells(df):
    assert calc_visibility_of_internal_cells(df) == 5




def test_calc_total_visible_cells(df):
    assert calc_total_visible_cells(df) == 21




def test_trees_visible_north(df):
    assert calc_trees_visible_north(df, (1,2)) == 1
    assert calc_trees_visible_north(df, (3,2)) == 2

def test_trees_visible_south(df):
    assert calc_trees_visible_south(df, (1,2)) == 2
    assert calc_trees_visible_south(df, (3,2)) == 1

def test_trees_visible_west(df):
    assert calc_trees_visible_west(df, (1,2)) == 1
    assert calc_trees_visible_west(df, (3,2)) == 2

def test_trees_visible_east(df):
    assert calc_trees_visible_east(df, (1,2)) == 2
    assert calc_trees_visible_east(df, (3,2)) == 2



def test_calc_scenic_score(df):
    assert calc_scenic_score(df, (1,2)) == 4
    assert calc_scenic_score(df, (3,2)) == 8