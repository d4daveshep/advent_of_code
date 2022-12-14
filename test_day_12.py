import networkx as nx
import pytest

@pytest.fixture()
def data_1():
    with open("./day_12_test_data.txt") as data_file:
        data = data_file.readlines()
    return data


def build_grid_of_nodes(lines: list) -> (list, nx.Graph):
    grid = []
    graph = nx.Graph()
    for row_num in range(len(lines)):
        row = []
        row_str_list = list(lines[row_num])
        for col_num in range(len(row_str_list)):
            node = graph.add_node((row_num,col_num,row_str_list[col_num]))
            row.append(node)
        grid.append(row)
    return grid, graph


def test_build_grid(data_1):
    grid = build_grid(data_1)
    assert len(grid) == len(data_1)
    assert grid[0][0] == "S"
    assert grid[2][5] == "E"

@pytest.fixture()
def grid(data_1):
    return build_grid(data_1)

def test_adjacent(grid):
    adjacents = get_adjacents(0,0)
    assert len(adjacents) == 2
    assert


def build_graph(graph, grid)-> nx.Graph:
    grid = build_grid(data_1)



def test_simple_graph(data_1):
    graph = nx.Graph()
    grid = build_grid(data_1)
    graph = build_graph(graph, grid)



