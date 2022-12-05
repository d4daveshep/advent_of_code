import pytest

from day_3 import priority, duplicate_char


def test_priority():
    assert priority("p") == 16
    assert priority("L") == 38
    assert priority("P") == 42
    assert priority("v") == 22
    assert priority("t") == 20
    assert priority("s") == 19

def test_find_duplicate_item():
    assert duplicate_char("vJrwpWtwJgWrhcsFMMfFFhFp") == "p"
    assert duplicate_char("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL") == "L"
    assert duplicate_char("PmmdzqPrVvPwwTWBwg") == "P"
    assert duplicate_char("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn") == "v"
    assert duplicate_char("ttgJtRGJQctTZtZT") == "t"
    assert duplicate_char("CrZsJsPPZsGzwwsLwLmpwMDw") == "s"





