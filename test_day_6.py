from collections import Counter

import pytest

from day_6 import find_first_marker, find_message_marker


def test_find_first_marker():

    assert find_first_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert find_first_marker("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert find_first_marker("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert find_first_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert find_first_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11

def test_find_message_marker():

    assert find_message_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert find_message_marker("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert find_message_marker("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert find_message_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert find_message_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26
