import pytest

from day_10 import Program


@pytest.fixture()
def data_1():
    with open("./day_10_data.txt") as data_file:
        data = data_file.readlines()
    return data



def test_5_cycles():
    data = ["noop\n", "addx 3\n", "addx -5\n"]
    program = Program()
    for line in data:
        program.process_instruction(line)
    assert program.x == -1
    assert program.cycles == 5
    assert program.signal_strength(1) == 1


def test_part_1_data(data_1):
    program = Program()
    program.process_instructions(data_1)
    assert program.signal_strength(20) == 420
    assert program.signal_strength(60) == 1140
    assert program.signal_strength(100) == 1800
    assert program.signal_strength(140) == 2940
    assert program.signal_strength(180) == 2880
    assert program.signal_strength(220) == 3960
    assert program.sum_signal_strength() == 13140
