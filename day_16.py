from itertools import permutations

import networkx as nx
import parse
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

def calc_total_flow(perm: tuple, valves:dict, graph:Graph) -> int:

    mins_remaining = 30
    start = "AA"
    total_flow_relieved = 0

    for end in perm:
        path_length = nx.shortest_path_length(graph, start, end)
        mins_remaining -= (path_length+1)
        total_flow_relieved += valves[end].flow * mins_remaining
        start = end

    return total_flow_relieved



