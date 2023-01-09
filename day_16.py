import functools
import time
from itertools import permutations

import networkx as nx
import parse
from aocd.models import Puzzle
from networkx import Graph


class Valve:
    def __init__(self, name=None, flow=0, neighbours=[]):
        self.neighbours = neighbours
        self.flow = flow
        self.name = name

    def __repr__(self):
        return f"Valve(name={self.name}, flow={self.flow}, neighbours={self.neighbours})"


class ParseError(Exception):
    pass


def parse_input_line(line: str) -> Valve:
    valve = Valve()
    if "tunnels" in line:
        result = parse.search("Valve {valve_name} has flow rate={flow:d}; tunnels lead to valves {to_valves:D}",
                              line.strip())
    elif "tunnel" in line:
        result = parse.search("Valve {valve_name} has flow rate={flow:d}; tunnel leads to valve {to_valves:D}",
                              line.strip())
    else:
        raise ParseError(line)

    valve.name = result.named["valve_name"]
    valve.flow = result.named["flow"]
    valve.neighbours = result.named["to_valves"].split(", ")
    return valve


def parse_data(data: list) -> dict:
    return {valve.name: valve for valve in [parse_input_line(line) for line in data]}


def build_graph(valves: dict) -> Graph:
    graph = nx.Graph()
    for valve in valves.values():
        for neighbour in valve.neighbours:
            graph.add_edge(valve.name, neighbour)
    return graph


def get_flow_valve_names(valves):
    return [v.name for v in filter(lambda v: v.flow > 0, valves.values())]


def get_flow_valve_permutations(flow_valve_names):
    return list(permutations(flow_valve_names, len(flow_valve_names)))


@functools.cache
def get_shortest_path_length(graph: Graph, start:str, end:str)-> int:
    return nx.shortest_path_length(graph, start, end)

def calc_total_flow(perm: tuple, valves: dict, graph: Graph) -> int:
    mins_remaining = 30
    start = "AA"
    total_flow_relieved = 0

    for end in perm:
        path_length = get_shortest_path_length(graph, start, end)
        mins_remaining -= (path_length + 1)
        if mins_remaining<0:
            break
        total_flow_relieved += valves[end].flow * mins_remaining
        start = end

    return total_flow_relieved


def parse_raw_data(puzzle_input: str) -> list:
    return puzzle_input.split('\n')


def solve_part_1(data: list) -> int:
    valves = parse_data(data)
    graph = build_graph(valves)
    # perms = get_flow_valve_permutations(get_flow_valve_names(valves))
    flow_valve_names = get_flow_valve_names(valves)
    perms = permutations(flow_valve_names, len(flow_valve_names))

    max_flow_relieved = 0
    counter = 0
    for perm in perms:
        counter += 1
        # if counter > 10e7:
        #     break
        if counter % 1000000 == 0:
            print(f"\rperm# {counter}, max flow = {max_flow_relieved}", end="")
        max_flow_relieved = max([max_flow_relieved, calc_total_flow(perm, valves, graph)])

    return max_flow_relieved


def solve_part_2(data: list) -> int:
    pass


if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=16)
    puzzle_input = puzzle.input_data
    data = parse_raw_data(puzzle_input)

    tic = time.perf_counter()
    part_1_answer = solve_part_1(data)
    toc = time.perf_counter()
    print(f"\nPart 1 answer = {part_1_answer}")
    print(f"took {(toc - tic) * 1000:0.1f} msec")

    tic = time.perf_counter()
    part_2_answer = solve_part_2(data)
    toc = time.perf_counter()
    print(f"Part 2 answer = {part_2_answer}")
    print(f"took {(toc - tic) * 1000:0.1f} msec")
