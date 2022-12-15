import networkx as nx
import pytest
from networkx import nodes

from day_12 import build_grid, build_grid_of_tuples, build_graph, get_adjacent_cells, find_start_end


@pytest.fixture()
def data_1():
    with open("./day_12_test_data.txt") as data_file:
        data = data_file.readlines()
    return data


@pytest.fixture()
def grid(data_1):
    return build_grid(data_1)


@pytest.fixture()
def tuples_grid(grid):
    return build_grid_of_tuples(grid)


def test_build_grid(data_1):
    grid = build_grid(data_1)
    grid = build_grid_of_tuples(grid)
    assert len(grid) == len(data_1)
    assert grid[0][0] == (0, 0, "`")
    assert grid[2][5] == (2, 5, "{")


def test_build_graph(tuples_grid):
    graph = build_graph(tuples_grid)
    start, end = find_start_end(tuples_grid)
    assert len(nodes(graph)) == 40
    assert len(graph) == 40
    assert graph.has_node((0, 0, "`"))
    assert graph.has_edge((0, 0, "`"), (0, 1, 'a'))
    assert not graph.has_edge((0, 2, "b"), (0, 3, "q"))


def test_shortest_path_length(tuples_grid):
    graph = build_graph(tuples_grid)
    start, end = find_start_end(tuples_grid)
    path = nx.shortest_path(graph, source=start, target=end)
    assert len(path) == 32

def test_find_start_end(tuples_grid):
    start, end = find_start_end(tuples_grid)
    assert start == (0,0,'`')
    assert end == (2,5,'{')

def test_nx_graph():
    graph = nx.Graph()
    t1 = (1, 1, "a")
    t2 = (2, 2, "b")
    graph.add_node(t1)
    graph.add_node(t2)

    assert graph.has_node(t1)
    assert graph.has_node(t2)

    graph.add_edge(t1, t2)
    assert graph.has_edge(t1, t2)
    assert graph.has_edge(t2, t1)

    the_nodes = iter(nodes(graph))
    n = next(the_nodes)

    assert n == t1

    pass


def test_get_adjacents(tuples_grid):
    adjacents = get_adjacent_cells((3, 3), tuples_grid)
    assert len(adjacents) == 4
    assert (2, 3, "s") in adjacents
    assert (4, 3, "e") in adjacents
    assert (3, 2, "c") in adjacents
    assert (3, 4, "u") in adjacents

    adjacents = get_adjacent_cells((0, 0), tuples_grid)
    assert len(adjacents) == 2
    assert (0, 1, "a") in adjacents
    assert (1, 0, "a") in adjacents

    adjacents = get_adjacent_cells((0, 7), tuples_grid)
    assert len(adjacents) == 2
    assert (0, 6, "n") in adjacents
    assert (1, 7, "l") in adjacents

    adjacents = get_adjacent_cells((4, 0), tuples_grid)
    assert len(adjacents) == 2
    assert (3, 0, "a") in adjacents
    assert (4, 1, "b") in adjacents

    adjacents = get_adjacent_cells((4, 7), tuples_grid)
    assert len(adjacents) == 2
    assert (3, 7, "j") in adjacents
    assert (4, 6, "h") in adjacents
