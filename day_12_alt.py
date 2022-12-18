# alternate solution for Day 12 using my own Graph structure
import time
from typing import NamedTuple

from aocd.models import Puzzle


class Node(NamedTuple):
    row: int
    col: int
    label: str


class Graph:
    def __init__(self, directional=True):
        self.directional = directional
        self.nodes = []
        self.edges = {}

    def __len__(self):
        return len(self.nodes)

    def __getitem__(self, item):
        i = self.nodes.index(item)
        return self.nodes[i]

    def __contains__(self, item):
        return item in self.nodes

    def add_node(self, n1: Node):
        if n1 in self.nodes:
            raise KeyError(f"Graph already contains node:{n1}")
        else:
            self.nodes.append(n1)

    def add_nodes(self, node_list: list):
        for node in node_list:
            self.add_node(node)

    def add_edge(self, source, target):
        for n in [source, target]:
            if n not in self.nodes:
                self.add_node(n)
        if source not in self.edges:
            self.edges[source] = [target]
        elif target in self.edges[source]:
            raise KeyError(f"Edge between {source} and {target} already exists")
        else:
            self.edges[source].append(target)
        if not self.directional:
            self.add_edge(target, source)

    def has_edge(self, source, target):
        return source in self.edges and target in self.edges[source]

    def has_path(self, start: Node, end: Node):
        path = self.find_path(start, end)
        if len(path) > 0:
            return True
        else:
            return False

    def find_path(self, start: Node, end: Node, path=[]):
        path = path + [start]
        if start == end:
            return path
        for node in self.edges[start]:
            if node not in path:
                new_path = self.find_path(node, end, path)
                if new_path:
                    return new_path

    def find_all_paths(self, start: Node, end: Node, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in self.edges[start]:
            new_paths=[]
            if node not in path:
                new_paths = self.find_all_paths(node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
        return paths

    def shortest_path_length(self, start, end):
        paths = self.find_all_paths(start,end)
        shortest_length = min([len(path) for path in paths])
        return shortest_length

    def find_shortest_path(self, start, end, path=[]):
        print(f"start={start}, end={end}, path_len={len(path)}")
        path = path + [start]
        if start == end:
            return path
        if start not in self.edges:
            return None
        shortest = None
        for node in self.edges[start]:
            if node not in path:
                new_path = self.find_shortest_path(node, end, path)
                if new_path:
                    if not shortest or len(new_path) < len(shortest):
                        shortest = new_path
        if shortest:
            print(f"shortest={len(shortest)}")
        return shortest

def build_grid(lines: list) -> list:
    grid = []
    for line in lines:
        row = list(line.strip())
        grid.append(row)
    return grid



def build_graph(nodes_grid):
    graph = Graph()
    # first pass to create the nodes
    print("doing first pass")
    for row_num in range(len(nodes_grid)):
        for col_num in range(len(nodes_grid[row_num])):
            n = nodes_grid[row_num][col_num]
            graph.add_node(n)

    # second pass to create the edges
    print("doing second pass")
    for row_num in range(len(nodes_grid)):
        for col_num in range(len(nodes_grid[row_num])):
            print(f"({row_num},{col_num})")
            n1 = nodes_grid[row_num][col_num]
            adjacents = get_adjacent_cells((row_num, col_num), nodes_grid)

            for n2 in adjacents:
                if graph.has_edge(n1, n2):
                    continue
                else:
                    r1, c1, height1 = n1
                    r2, c2, height2 = n2
                    # if ord(n1.label) - 1 <= ord(n2.label) and ord(n2.label) <= ord(n1.label) + 1:
                    if ord(n1.label) == ord(n2.label) or ord(n1.label) == ord(n2.label)-1:
                        graph.add_edge(n1, n2)
    print("done building graph")
    return graph

def find_start_end(tuples_grid) -> tuple:
    start = None
    end = None
    for row_num in range(len(tuples_grid)):
        for col_num in range(len(tuples_grid[row_num])):
            tup = tuples_grid[row_num][col_num]
            r, c, height = tup
            if height == '`':
                start = Node(row=r, col=c, label=height)
                continue
            if height == '{':
                end = Node(row=r, col=c, label=height)
                continue
            if start and end:
                break

    return start, end


def build_grid_of_nodes(grid) -> list:
    for row_num in range(len(grid)):
        for col_num in range(len(grid[row_num])):
            height = grid[row_num][col_num]
            if height == "S":
                height = chr(ord("a") - 1)
            elif height == "E":
                height = chr(ord("z") + 1)

            grid[row_num][col_num] = Node(row_num, col_num, height)
    return grid

def get_adjacent_cells(row_col: tuple, nodes_grid: list) -> list:
    row, col = row_col
    max_row = len(nodes_grid) - 1
    max_col = len(nodes_grid[0]) - 1
    adjacent_cells = []
    if 0 < row:
        adjacent_cells.append(nodes_grid[row - 1][col])
    if row < max_row:
        adjacent_cells.append(nodes_grid[row + 1][col])
    if 0 < col:
        adjacent_cells.append(nodes_grid[row][col - 1])
    if col < max_col:
        adjacent_cells.append(nodes_grid[row][col + 1])
    return adjacent_cells


def parse(puzzle_input: str) -> list:
    return puzzle_input.split('\n')


def solve_part_1(data: list) -> int:
    grid = build_grid(data)
    nodes_grid = build_grid_of_nodes(grid)
    start, end = find_start_end(nodes_grid)
    graph = build_graph(nodes_grid)
    # assert graph.has_path(start, end)
    print("doing shortest now...")
    # shortest = graph.shortest_path_length(start, end)
    shortest = graph.find_shortest_path(start, end)

    return len(shortest) - 1

def solve_part_2(data: list) -> int:
    pass


if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=12)
    puzzle_input = puzzle.input_data
    data = parse(puzzle_input)

    tic = time.perf_counter()
    part_1_answer = solve_part_1(data)
    toc = time.perf_counter()
    print(f"Part 1 answer = {part_1_answer}")
    print(f"took {(toc - tic) * 1000:0.1f} msec")

    tic = time.perf_counter()
    part_2_answer = solve_part_2(data)
    toc = time.perf_counter()
    print(f"Part 2 answer = {part_2_answer}")
    print(f"took {(toc - tic) * 1000:0.1f} msec")

