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


def draw_sprite(crt_row:list, cycle: int, x: int) -> list:
    if x - 1 <= cycle <= x + 1:
        crt_row[cycle - 1] = "#"
    return crt_row


def display(crt_row:list)->str:
    return "".join([str(i) for i in crt_row])


def test_draw_sprite():
    crt_row = ["." for i in range(40)]
    cycle = 1
    x = 1
    crt_row = draw_sprite(crt_row, cycle, x)
    assert crt_row[0] == "#"
    print(display(crt_row))

def test_crt_row_1(data_1):
    crt_row = ["." for i in range(40)]

    program = Program()
    program.process_instructions(data_1)
    for cycle in range(1,41):
        x = program.history[cycle]
        draw_sprite(crt_row, cycle, x)
    print(display(crt_row))