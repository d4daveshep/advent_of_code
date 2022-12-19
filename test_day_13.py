from collections import deque

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


def make_deque(item) -> deque:
    if isinstance(int, type(item)):
        return deque(list(item))
    elif isinstance(list, type(list)):
        return deque(item)
    else:
        raise TypeError(f"{item} is not an int or list")


def is_order_correct(left_list: list, right_list: list) -> bool:
    # convert both to deques
    left_list = make_deque(left_list)
    right_list = make_deque(right_list)

    while True:
        try:
            left_val = left_list.popleft()
        except IndexError:
            return True

        try:
            right_val = right_list.popleft()
        except IndexError:
            return False

        if left_val < right_val:
            return True
        if left_val > right_val:
            return False


def make_list(item):
    if isinstance(int, type(item)):
        return list(item)
    elif isinstance(list, type(list)):
        return item
    else:
        raise TypeError(f"{item} is not an int or list")


def compare(left, right) -> bool:
    left = make_deque(left)
    right = make_deque(right)

    try:
        answer = left<right
        return answer
    except TypeError:
        return compare(left.popleft(), right.popleft())



def test_compare_left_right_lists(data_pairs):
    # left, right = data_pairs[0]
    # assert is_order_correct(left, right)

    # left, right = data_pairs[1]
    # assert is_order_correct(left, right)

    for i in range(len(data_pairs)):
        left, right = data_pairs[i]
        answer = compare(left, right)
        print(f"{i + 1}, {answer}")
