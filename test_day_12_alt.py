import pytest

from day_12 import build_grid, get_adjacent_cells
from day_12_alt import Node, Graph, find_start_end, build_grid_of_nodes, build_graph


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


def test_graph():
    n1 = Node(row=0, col=0, label='S')
    n2 = Node(row=0, col=1, label='a')
    n3 = Node(row=0, col=2, label='b')
    n4 = Node(row=0, col=3, label='q')

    graph = Graph(directional=True)
    graph.add_node(n1)
    graph.add_node(n2)
    graph.add_nodes([n3, n4])

    assert len(graph) == 4
    assert n1 in graph
    assert n3 in graph


def test_edge_directional():
    n1 = Node(row=0, col=0, label='S')
    n2 = Node(row=0, col=1, label='a')
    n3 = Node(row=0, col=2, label='b')
    n4 = Node(row=0, col=3, label='q')

    graph = Graph(directional=True)
    graph.add_nodes([n1, n2, n3, n4])

    graph.add_edge(n1, n2)
    assert graph.has_edge(n1, n2)
    with pytest.raises(KeyError):
        graph.add_edge(n1, n2)

    graph.add_edge(n2, n3)
    graph.add_edge(n3, n2)
    assert graph.has_edge(n2, n3) and graph.has_edge(n3, n2)


def test_edge_non_directional():
    n1 = Node(row=0, col=0, label='S')
    n2 = Node(row=0, col=1, label='a')
    n3 = Node(row=0, col=2, label='b')
    n4 = Node(row=0, col=3, label='q')

    graph = Graph(directional=False)
    graph.add_nodes([n1, n2, n3, n4])

    graph.add_edge(n1, n2)
    assert graph.has_edge(n1, n2)
    with pytest.raises(KeyError):
        graph.add_edge(n1, n2)

    graph.add_edge(n2, n3)
    with pytest.raises(KeyError):
        graph.add_edge(n3, n2)
    assert graph.has_edge(n2, n3)
    assert not graph.has_edge(n3, n2)




def test_build_graph(nodes_grid):
    graph = build_graph(nodes_grid)
    start, end = find_start_end(nodes_grid)

    assert len(graph) == 40
    assert start in graph
    assert end in graph

    n1 = Node(0, 1, 'a')

    assert graph.has_edge(start, n1)
    assert graph.has_path(start, end)
    path = graph.find_path(start, end)
    paths = graph.find_all_paths(start, end)
    assert graph.shortest_path_length(start, end) == 32
    assert len(graph.find_shortest_path(start, end)) == 32
