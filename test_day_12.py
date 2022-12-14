import networkx as nx
import pytest
from networkx import nodes


@pytest.fixture()
def data_1():
    with open("./day_12_test_data.txt") as data_file:
        data = data_file.readlines()
    return data

@pytest.fixture()
def grid(data_1):
    return build_grid(data_1)




def build_graph(grid: list) -> nx.Graph:
    graph = nx.Graph()
    for row_num in range(len(grid)):
        for col_num in range(len(grid[row_num])):
            tup = (row_num,col_num,grid[row_num][col_num])

            # adjacents = get_adjacents((row_num,col_num), grid)

            node = graph.add_node(tup)
    return graph


def build_grid(lines:list)-> list:
    grid = []
    for line in lines:
        row = list(line.strip())
        grid.append(row)
    return grid

def build_grid_of_tuples(grid)-> list:
    for row_num in range(len(grid)):
        for col_num in range(len(grid[row_num])):
            height = grid[row_num][col_num]
            grid[row_num][col_num] = (row_num,col_num,height)
    return grid


def test_build_grid(data_1):
    grid = build_grid(data_1)
    grid = build_grid_of_tuples(grid)
    assert len(grid) == len(data_1)
    assert grid[0][0] == (0,0,"S")
    assert grid[2][5] == (2,5,"E")

def test_build_graph(grid):
    graph = build_graph(grid)
    assert len(nodes(graph)) == 40
    assert len(graph) == 40
#
# def test_adjacent(grid):
#     adjacents = get_adjacents(0,0)
#     assert len(adjacents) == 2
#     assert

def test_nx_graph():
    graph = nx.Graph()
    t1 = (1,1,"a")
    t2 = (2,2,"b")
    graph.add_node(t1)
    graph.add_node(t2)

    assert graph.has_node(t1)
    assert graph.has_node(t2)

    graph.add_edge(t1,t2)
    assert graph.has_edge(t1,t2)

    print(graph)






