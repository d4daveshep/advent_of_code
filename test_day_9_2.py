import pytest

from day_9 import Point, Move, Rope, Vector, move_map


@pytest.fixture()
def data() -> list:
    with open("./day_9_2_data.txt") as data_file:
        data = data_file.readlines()
    return data

def test_move_R_5():
    rope = Rope10(head=Point(0,0))
    rope.do_move("R_5")
    assert rope.head == Point(5,0)
    assert rope.p0 == Point(5,0)
    assert rope.p1 == Point(4,0)
    assert rope.p9 == Point(0,0)
    assert rope.tail == Point(0.0)