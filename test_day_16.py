import networkx as nx
import pytest

from day_16 import parse_input_line, parse_data, build_graph, get_flow_valve_names, get_flow_valve_permutations


@pytest.fixture()
def test_data():
    with open("./day_16_test_data.txt") as data_file:
        data = data_file.readlines()
    return data


def test_parse_input_line():
    line1 = "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB"
    line2 = "Valve HH has flow rate=22; tunnel leads to valve GG"

    valve_AA = parse_input_line(line1)
    assert valve_AA.name == "AA"
    assert valve_AA.flow == 0
    assert valve_AA.neighbours == ["DD", "II", "BB"]

    valve_HH = parse_input_line(line2)
    assert valve_HH.name == "HH"
    assert valve_HH.flow == 22
    assert valve_HH.neighbours == ["GG"]


def test_parse_test_data(test_data):
    valves = parse_data(test_data)
    assert len(valves) == 10


def test_build_graph(test_data):
    valves = parse_data(test_data)
    graph = build_graph(valves)
    assert len(graph.nodes) == 10
    assert len(graph.edges) == 10
    assert nx.shortest_path_length(graph, "JJ", "HH") == 7


def test_permutations_of_flow_valves(test_data):
    valves = parse_data(test_data)
    flow_valve_names = get_flow_valve_names(valves)
    assert len(flow_valve_names) == 6
    perms = get_flow_valve_permutations(flow_valve_names)
    assert len(perms) == 720
