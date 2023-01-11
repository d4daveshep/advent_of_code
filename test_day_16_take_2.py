import functools
from dataclasses import dataclass

import networkx as nx
import pytest
from aocd.models import Puzzle
from networkx import Graph

from day_16 import parse_data, build_graph, get_flow_valve_names, parse_raw_data


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


@dataclass
class State:
    permutation: list
    # current_flow: int
    cumulative_flow: int
    mins_remaining: int


@functools.cache
def get_shortest_path_length(graph: Graph, start: str, end: str) -> int:
    return nx.shortest_path_length(graph, start, end)


def calc_total_flow(perm: tuple, valves: dict, graph: Graph) -> (int, int):
    mins_remaining = 30
    start = perm[0]
    total_flow_relieved = 0

    for end in perm[1:]:
        path_length = get_shortest_path_length(graph, start, end)
        mins_remaining -= (path_length + 1)
        if mins_remaining < 0:
            break
        total_flow_relieved += valves[end].flow * mins_remaining
        start = end

    return total_flow_relieved, mins_remaining


def test_build_state_dict(test_data):
    valves = parse_data(test_data)
    graph = build_graph(valves)
    flow_valve_names = get_flow_valve_names(valves)

    best_max_flow = 0
    state_dict = {}

    permutation = ["AA", "BB"]

    flow, mins = calc_total_flow(tuple(permutation), valves, graph)
    assert flow == 13 * 28
    assert mins == 28

    state_dict[tuple(permutation)] = State(permutation, flow, mins)
    best_max_flow = max(best_max_flow, flow)

    permutation.append("CC")
    flow, mins = calc_total_flow(tuple(permutation), valves, graph)
    assert flow == 13 * 28 + 2 * 26
    assert mins == 26

    state_dict[tuple(permutation)] = State(permutation, flow, mins)
    best_max_flow = max(best_max_flow, flow)
    assert best_max_flow == flow

    pass


class ValveNetwork:
    def __init__(self, data: list):
        self.valves = parse_data(data)
        self.graph = build_graph(self.valves)
        self.flow_valves = get_flow_valve_names(self.valves)

        self.state_dict = {}
        self.best_max_flow = 0

    def do_permutations(self):
        permutation = ["AA"]

        positions = [False] * (len(self.flow_valves)+1)
        positions[0] = True

        self.generate(permutation, self.flow_valves, positions)

    def generate(self, permutation: list, elements: list, positions: list):
        # if len(permutation) == len(elements)+1:
        # print(permutation)
        #     pass
        #
        # else:
        for i in range(0, len(elements)+1):

            if positions[i]:
                continue

            # Set the position (taken), append the element
            positions[i] = True
            permutation.append(elements[i-1])
            print(permutation)

            #  check state here ?
            flow, mins = self.calc_total_flow(permutation)
            self.state_dict[tuple(permutation)] = State(permutation, flow, mins)
            if flow > self.best_max_flow:
                self.best_max_flow = flow
                print(f"best max = {self.best_max_flow} at {permutation}")

            self.generate(permutation, elements, positions)

            # Remove the element, reset the position (available),
            permutation.pop()
            positions[i] = False

    def get_max_flow(self) -> int:
        pass

    def calc_total_flow(self, permutation):
        mins_remaining = 30
        start = permutation[0]
        total_flow_relieved = 0

        for end in permutation[1:]:
            path_length = get_shortest_path_length(self.graph, start, end)
            mins_remaining -= (path_length + 1)
            if mins_remaining < 0:
                break
            total_flow_relieved += self.valves[end].flow * mins_remaining
            start = end

        return total_flow_relieved, mins_remaining


def test_do_permutations(test_data):
    valve_network = ValveNetwork(test_data)
    print()
    valve_network.do_permutations()
    # valve_network.
