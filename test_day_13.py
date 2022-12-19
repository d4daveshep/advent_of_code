import pytest

from day_13 import parse_data_pairs, compare


@pytest.fixture()
def test_data():
    with open("./day_13_test_data.txt") as data_file:
        data = data_file.readlines()
    return data


def parse_packet(packet_str: str) -> list:
    # r = repr(packet_str)
    l = eval(packet_str)
    return l


def test_create_list_from_string():
    packet_str = "[1,1,3,1,1]"
    packet_list = parse_packet(packet_str)
    assert packet_list == [1, 1, 3, 1, 1]

    packet_str = "[[1],[2,3,4]]"
    packet_list = parse_packet(packet_str)
    assert packet_list == [[1], [2, 3, 4]]
    pass

    packet_str = "[[[]]]"
    packet_list = parse_packet(packet_str)
    assert packet_list == [[[]]]

    packet_str = "[[4,4],4,4,4]"
    packet_list = parse_packet(packet_str)
    assert packet_list == [[4, 4], 4, 4, 4]


def test_parse_data_pairs(test_data):
    data_pairs = parse_data_pairs(test_data)
    assert len(data_pairs) == 8
    assert data_pairs[0] == ([1, 1, 3, 1, 1], [1, 1, 5, 1, 1])
    assert data_pairs[7] == ([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9])


@pytest.fixture()
def data_pairs(test_data):
    return parse_data_pairs(test_data)


def test_compare(data_pairs):
    print()
    sum_total = 0
    for i in range(len(data_pairs)):
        left, right = data_pairs[i]
        answer = compare(left, right)
        if answer == -1:
            sum_total += i + 1

    print(f"sum_total = {sum_total}")
