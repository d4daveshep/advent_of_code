import pytest

from day_10 import Program, Display


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

    assert program.x_during_cycle(1) == 1
    assert program.x_after_cycle(1) == 1

    assert program.x_during_cycle(2) == 1
    assert program.x_after_cycle(2) == 1

    assert program.x_during_cycle(3) == 1
    assert program.x_after_cycle(3) == 4

    assert program.x_during_cycle(4) == 4
    assert program.x_after_cycle(4) == 4

    assert program.x_during_cycle(5) == 4
    assert program.x_after_cycle(5) == -1

    assert program.cycles == 5
    assert program.signal_strength_during_cycle(1) == 1


def test_part_1_data(data_1):
    program = Program()
    program.process_instructions(data_1)

    assert program.x_during_cycle(20) == 21
    assert program.x_during_cycle(60) == 19
    assert program.x_during_cycle(100) == 18
    assert program.x_during_cycle(140) == 21
    assert program.x_during_cycle(180) == 16
    assert program.x_during_cycle(220) == 18

    assert program.signal_strength_during_cycle(20) == 420
    assert program.signal_strength_during_cycle(60) == 1140
    assert program.signal_strength_during_cycle(100) == 1800
    assert program.signal_strength_during_cycle(140) == 2940
    assert program.signal_strength_during_cycle(180) == 2880
    assert program.signal_strength_during_cycle(220) == 3960
    assert program.sum_signal_strength() == 13140


def test_crt_row_1(data_1):
    crt_row = ["." for i in range(40)]

    program = Program()
    program.process_instructions(data_1)

    display = Display()

    for cycle in range(1, 240):
        x = program.x_during_cycle(cycle)
        display.draw_sprite(cycle, x)

    display.draw_rows()


def test_display_all_rows():
    display = Display()
    display.draw_rows()
    display.draw_sprite(1, 1)
    display.draw_sprite(39, 39)
    display.draw_sprite(40, 40)
    display.draw_sprite(41, 1)
    display.draw_sprite(240,40)
    display.draw_rows()
