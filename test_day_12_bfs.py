import pytest

from day_12_bfs import build_grid, build_grid_of_nodes, Node, find_start_end, find_valid_unvisited_adjacents, \
    find_nodes_at_step, do_next_step, print_graph, find_nodes_with_label


@pytest.fixture()
def data_1():
    with open("./day_12_test_data.txt") as data_file:
        data = data_file.readlines()
    return data


@pytest.fixture()
def grid(data_1):
    return build_grid(data_1)


@pytest.fixture()
def nodes_grid(grid):
    return build_grid_of_nodes(grid)


def test_node():
    n1 = Node(row=0, col=0, label='S')
    assert n1.row == 0
    assert n1.col == 0
    assert n1.label == 'S'
    n1.visited = False
    assert not n1.visited

    n2 = Node(1, 1, 'T')
    assert n1.can_move_to(n1)
    n3 = Node(3, 3, 'S')
    assert n1.can_move_to(n3)


def test_find_start_end(nodes_grid):
    start, end = find_start_end(nodes_grid)
    assert start == Node(0, 0, '`')
    assert end == Node(2, 5, '{')


def test_find_valid_unvisited_adjacents(nodes_grid):
    adjacents = find_valid_unvisited_adjacents(nodes_grid, nodes_grid[1][1])
    assert len(adjacents) == 4
    assert nodes_grid[0][1] in adjacents
    assert nodes_grid[1][0] in adjacents
    assert nodes_grid[2][1] in adjacents
    assert nodes_grid[1][2] in adjacents

    nodes_grid[1][2].visited = True
    adjacents = find_valid_unvisited_adjacents(nodes_grid, nodes_grid[1][1])
    assert len(adjacents) == 3
    assert nodes_grid[0][1] in adjacents
    assert nodes_grid[1][0] in adjacents
    assert nodes_grid[2][1] in adjacents
    assert nodes_grid[1][2] not in adjacents

    nodes_grid[1][2].visited = False
    adjacents = find_valid_unvisited_adjacents(nodes_grid, nodes_grid[2][2])
    assert len(adjacents) == 3
    assert nodes_grid[1][2] in adjacents
    assert nodes_grid[2][1] in adjacents
    assert nodes_grid[3][2] in adjacents
    assert nodes_grid[2][3] not in adjacents


def test_find_nodes_at_step(nodes_grid):
    nodes_grid[0][0].step = 0
    nodes_grid[1][0].step = 1
    nodes_grid[0][1].step = 1
    nodes_grid[0][2].step = 2
    nodes_grid[2][0].step = 2
    nodes_grid[1][1].step = 2

    nodes_0 = find_nodes_at_step(nodes_grid, 0)
    nodes_1 = find_nodes_at_step(nodes_grid, 1)
    nodes_2 = find_nodes_at_step(nodes_grid, 2)

    assert len(nodes_0) == 1
    assert len(nodes_1) == 2
    assert len(nodes_2) == 3

    assert nodes_grid[0][0] in nodes_0
    assert nodes_grid[0][1] in nodes_1
    assert nodes_grid[1][0] in nodes_1
    assert nodes_grid[1][1] in nodes_2
    assert nodes_grid[2][0] in nodes_2
    assert nodes_grid[0][2] in nodes_2


def test_next_step(nodes_grid):
    start, end = find_start_end(nodes_grid)

    start.step = 0
    start.visited = True

    do_next_step(nodes_grid, 0)
    assert nodes_grid[0][1].step == 1
    assert nodes_grid[1][0].step == 1
    assert nodes_grid[0][1].visited == True
    assert nodes_grid[1][0].visited == True


def test_do_next_step_until_end(nodes_grid):
    start, end = find_start_end(nodes_grid)
    start.step = 0
    end.step = -1
    start.visited = True

    print_graph(nodes_grid)

    step_num = 0
    while end.step == -1:
        print(f"step: {step_num}")
        do_next_step(nodes_grid, step_num)
        step_num += 1
        # if step_num % 20 == 0:
        print_graph(nodes_grid)
        # input("enter to continue")

    print_graph(nodes_grid)
    assert end.step == 31



def test_set_multiple_starting_points(nodes_grid):
    start, end = find_start_end(nodes_grid)
    start.step = 0
    end.step = -1
    start.visited = True

    nodes_a = find_nodes_with_label(nodes_grid,'a')
    assert len(nodes_a) == 5
    for node in nodes_a:
        node.step = 0
        node.visited = True

    step_num = 0
    while end.step == -1:
        print(f"step: {step_num}")
        do_next_step(nodes_grid, step_num)
        step_num += 1
        # if step_num % 20 == 0:
        # print_graph(nodes_grid)
        # input("enter to continue")

    print_graph(nodes_grid)
    assert end.step == 29

