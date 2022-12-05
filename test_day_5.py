from collections import deque

import pytest

from day_5 import do_move_for_part_1, get_final_state, do_move_for_part_2


@pytest.fixture
def stacks():
    stacks = []
    stacks.append(deque("ZN"))
    stacks.append(deque("MCD"))
    stacks.append(deque("P"))
    return stacks



def test_moves_part_1(stacks):
    do_move_for_part_1(stacks, "move 1 from 2 to 1")
    do_move_for_part_1(stacks, "move 3 from 1 to 3")
    do_move_for_part_1(stacks, "move 2 from 2 to 1")
    do_move_for_part_1(stacks, "move 1 from 1 to 2")

    final_state = get_final_state(stacks)

    assert final_state == "CMZ"

def test_moves_part_2(stacks):
    do_move_for_part_2(stacks, "move 1 from 2 to 1")
    do_move_for_part_2(stacks, "move 3 from 1 to 3")
    do_move_for_part_2(stacks, "move 2 from 2 to 1")
    do_move_for_part_2(stacks, "move 1 from 1 to 2")

    final_state = get_final_state(stacks)

    assert final_state == "MCD"




