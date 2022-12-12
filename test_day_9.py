import pytest

from day_9 import Point, Move, Rope, Vector, move_map


@pytest.fixture()
def data() -> list:
    with open("./day_9_data.txt") as data_file:
        data = data_file.readlines()
    return data


def test_move_up():
    head = Point(0, 0)
    assert head.move(Move.UP) == Point(0, 1)


def test_move_down():
    head = Point(0, 0)
    assert head.move(Move.DOWN) == Point(0, -1)


def test_move_left():
    head = Point(0, 0)
    assert head.move(Move.LEFT) == Point(-1, 0)


def test_move_right():
    head = Point(0, 0)
    assert head.move(Move.RIGHT) == Point(1, 0)


def test_tail_follows_head():
    rope = Rope(head=Point(0, 0), tail=Point(0, 0))
    rope.move_head(Move.RIGHT)
    assert rope.head == Point(1, 0)
    assert rope.tail == Point(0, 0)
    rope.move_head(Move.RIGHT)
    assert rope.head == Point(2, 0)
    assert rope.tail == Point(1, 0)
    rope.move_head(Move.UP)
    assert rope.head == Point(2, 1)
    assert rope.tail == Point(1, 0)
    rope.move_head(Move.UP)
    assert rope.head == Point(2, 2)
    assert rope.tail == Point(2, 1)
    rope.move_head(Move.RIGHT)
    rope.move_head(Move.RIGHT)
    assert rope.head == Point(4, 2)
    assert rope.tail == Point(3, 2)
    rope.move_head(Move.DOWN)
    rope.move_head(Move.DOWN)
    assert rope.head == Point(4, 0)
    assert rope.tail == Point(4, 1)
    rope.move_head(Move.LEFT)
    rope.move_head(Move.LEFT)
    assert rope.head == Point(2, 0)
    assert rope.tail == Point(3, 0)
    rope.move_head(Move.UP)
    rope.move_head(Move.UP)
    assert rope.head == Point(2, 2)
    assert rope.tail == Point(2, 1)


def test_gap_between_head_and_tail():
    rope = Rope(head=Point(0, 0), tail=Point(0, 0))
    assert rope.gap_tail_to_head() == (0, 0)
    assert rope.tail.gap_to(rope.head) == Vector(0, 0)

    rope = Rope(head=Point(1, 1), tail=Point(0, 0))
    assert rope.gap_tail_to_head() == Vector(1, 1)
    assert rope.tail.gap_to(rope.head) == Vector(1, 1)


def test_gap_between_points():
    assert Point(0, 0).gap_to(Point(1, 1)) == Vector(1, 1)
    assert Point(2, 1).gap_to(Point(1, 2)) == Vector(-1, 1)


def test_tail_is_adjacent_to_head():
    rope = Rope(head=Point(0, 0), tail=Point(0, 0))
    assert rope.tail_is_adjacent_to_head()
    rope = Rope(head=Point(1, 0), tail=Point(0, 0))
    assert rope.tail_is_adjacent_to_head()
    rope = Rope(head=Point(1, 1), tail=Point(0, 0))
    assert rope.tail_is_adjacent_to_head()
    rope = Rope(head=Point(-1, -1), tail=Point(0, 0))
    assert rope.tail_is_adjacent_to_head()
    rope = Rope(head=Point(2, 0), tail=Point(0, 0))
    assert not rope.tail_is_adjacent_to_head()
    rope = Rope(head=Point(2, 1), tail=Point(0, 0))
    assert not rope.tail_is_adjacent_to_head()
    rope = Rope(head=Point(-2, -1), tail=Point(0, 0))
    assert not rope.tail_is_adjacent_to_head()


def test_point_is_adjacent_to_other_point():
    assert Point(0, 0).is_adjacent_to(Point(0, 0))
    assert Point(1, 0).is_adjacent_to(Point(0, 0))
    assert Point(1, 1).is_adjacent_to(Point(0, 0))
    assert Point(-1, -1).is_adjacent_to(Point(0, 0))
    assert not Point(2, 0).is_adjacent_to(Point(0, 0))
    assert not Point(2, 1).is_adjacent_to(Point(0, 0))
    assert not Point(-2, 1).is_adjacent_to(Point(0, 0))


def test_close_gap():
    rope = Rope(head=Point(2, 2), tail=Point(1, 0))
    assert not rope.tail_is_adjacent_to_head()
    assert rope.gap_tail_to_head() == Vector(1, 2)
    rope.close_gap()
    # assert rope.tail == Point(2,1)


def test_data_moves(data):
    rope = Rope(head=Point(0, 0), tail=Point(0, 0))
    for line in data:
        line = line.strip()
        rope.do_multiple_moves(line)
    assert rope.head == Point(2, 2)
    assert rope.tail == Point(1, 2)
    assert rope.tail.count_unique_positions() == 13


def test_map_dir_to_move():
    assert move_map["U"] == Move.UP
    assert move_map["D"] == Move.DOWN
    assert move_map["L"] == Move.LEFT
    assert move_map["R"] == Move.RIGHT


def test_10_knot_rope():
    rope = Rope(knots=10)
    assert rope.num_knots == 10
    for i in range(rope.num_knots):
        assert rope.knot[i] == Point(0,0)
