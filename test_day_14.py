import pytest

from day_14 import parse_data_to_tuples_list


@pytest.fixture()
def test_data():
    with open("./day_14_test_data.txt") as data_file:
        data = data_file.readlines()
    return data


def test_parse_data(test_data):
    tuples_list = parse_data_to_tuples_list(test_data)
    assert len(tuples_list) == 2
    assert [(498,4),(498,6),(496,6)] in tuples_list