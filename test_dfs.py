import pytest

from day_16 import parse_data, Valve


@pytest.fixture()
def test_data():
    with open("./day_16_test_data.txt") as data_file:
        data = data_file.readlines()
    return data


def dfs(graph:dict, visited:set, valve:Valve):
    if valve not in visited:
        print(valve)
        visited.add(valve)
        for neighbour in valve.neighbours:
            dfs(graph, visited, graph[neighbour])


def test_dfs(test_data):
    graph = parse_data(test_data)
    visited = set()

    print()
    dfs(graph, visited, graph["AA"])

    pass