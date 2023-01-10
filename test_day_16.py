from itertools import permutations

import networkx as nx
import pytest
from aocd.models import Puzzle

from day_16 import parse_input_line, parse_data, build_graph, get_flow_valve_names, get_flow_valve_permutations, \
    calc_total_flow, parse_raw_data


@pytest.fixture()
def part_1_data():
    puzzle = Puzzle(year=2022, day=16)
    puzzle_input = puzzle.input_data
    data = parse_raw_data(puzzle_input)
    return data

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
    # perms = get_flow_valve_permutations(flow_valve_names)
    perms = permutations(flow_valve_names, len(flow_valve_names))
    assert len(list(perms)) == 720



def test_total_flow_relieved(test_data):
    valves = parse_data(test_data)
    graph = build_graph(valves)
    perm = ("DD", "BB", "JJ", "HH", "EE", "CC")

    assert calc_total_flow(perm, valves, graph) == 1651

def test_find_max_flow_relieved(test_data):
    valves = parse_data(test_data)
    graph = build_graph(valves)
    flow_valve_names = get_flow_valve_names(valves)
    perms = permutations(flow_valve_names, len(flow_valve_names))

    max_flow_relieved = 0
    for perm in perms:
        max_flow_relieved = max([max_flow_relieved, calc_total_flow(perm, valves, graph)])

    assert max_flow_relieved == 1651


def get_flow_by_distance(start, flow_valve_names, graph, valves )-> dict:
    pass


def test_all_pairs_shortest_path(test_data):
    valves = parse_data(test_data)
    graph = build_graph(valves)
    flow_valve_names = get_flow_valve_names(valves)

    paths = dict(nx.all_pairs_shortest_path(graph))
    lengths = dict(nx.all_pairs_shortest_path_length(graph))

    start = "AA"
    time_remaining = 30
    flow_by_distance = {}
    for end, dist in lengths["AA"].items():
        if valves[end].flow > 0:
            flow_by_distance[end] = valves[end].flow * (time_remaining - dist - 1)

    start = "JJ"
    time_remaining = 27
    flow_by_distance = {}
    for end, dist in lengths[start].items():
        if valves[end].flow > 0:
            flow_by_distance[end] = valves[end].flow * (time_remaining - dist - 1)

    start = "DD"
    time_remaining = 28
    flow_by_distance = {}
    for end, dist in lengths[start].items():
        if valves[end].flow > 0:
            flow_by_distance[end] = valves[end].flow * (time_remaining - dist - 1)

    pass




def test_part_1_data(part_1_data):
    valves = parse_data(part_1_data)
    graph = build_graph(valves)
    flow_valve_names = get_flow_valve_names(valves)

    paths = dict(nx.all_pairs_shortest_path(graph))
    lengths = dict(nx.all_pairs_shortest_path_length(graph))



    pass
