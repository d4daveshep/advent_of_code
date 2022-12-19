from collections import deque
from itertools import zip_longest

import pytest


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


def parse_data_pairs(test_data):
    data_deque = deque(test_data)
    data_pairs = []
    while len(data_deque):
        left = eval(data_deque.popleft())
        right = eval(data_deque.popleft())
        data_pairs.append((left, right))
        try:
            blank = data_deque.popleft()
        except IndexError:
            pass
    return data_pairs


def test_parse_data_pairs(test_data):
    data_pairs = parse_data_pairs(test_data)
    assert len(data_pairs) == 8
    assert data_pairs[0] == ([1, 1, 3, 1, 1], [1, 1, 5, 1, 1])
    assert data_pairs[7] == ([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9])


@pytest.fixture()
def data_pairs(test_data):
    return parse_data_pairs(test_data)


def compare(left, right) -> int:
    """
    Borrowed this solution.  it uses a few things i wouldn't normally use like walrus operator, zip function, ternery statements
    :param left: int or list or None
    :param right: int or list or None
    :return: -1 if left < right, +1 if left > right or 0 if left == right
    """
    # left or right could be None from zip_longest
    if left is None:
        return -1
    if right is None:
        return 1

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0

    elif isinstance(left, list) and isinstance(right, list):
        for l2, r2 in zip_longest(left, right):
            if (result := compare(l2, r2)) != 0:
                return result
        return 0

    else:
        l2 = [left] if isinstance(left, int) else left
        r2 = [right] if isinstance(right, int) else right
        return compare(l2, r2)



def test_compare(data_pairs):
    print()
    sum_total = 0
    for i in range(len(data_pairs)):
        left, right = data_pairs[i]
        answer = compare(left, right)
        if answer == -1:
            sum_total += i+1

    print(f"sum_total = {sum_total}")

