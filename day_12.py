import time

from aocd.models import Puzzle

import networkx as nx


def build_grid(lines: list) -> list:
    grid = []
    for line in lines:
        row = list(line.strip())
        grid.append(row)
    return grid


def build_grid_of_tuples(grid) -> list:
    for row_num in range(len(grid)):
        for col_num in range(len(grid[row_num])):
            height = grid[row_num][col_num]
            if height == "S":
                height = chr(ord("a") - 1)
            elif height == "E":
                height = chr(ord("z") + 1)

            grid[row_num][col_num] = (row_num, col_num, height)
    return grid


def find_start_end(tuples_grid) -> tuple:
    start = None
    end = None
    for row_num in range(len(tuples_grid)):
        for col_num in range(len(tuples_grid[row_num])):
            tup = tuples_grid[row_num][col_num]
            r, c, height = tup
            if height == '`':
                start = tup
                continue
            if height == '{':
                end = tup
                continue
            if start and end:
                break

    return start, end


def get_adjacent_cells(row_col: tuple, tuples_grid: list) -> list:
    row, col = row_col
    max_row = len(tuples_grid) - 1
    max_col = len(tuples_grid[0]) - 1
    adjacent_cells = []
    if 0 < row:
        adjacent_cells.append(tuples_grid[row - 1][col])
    if row < max_row:
        adjacent_cells.append(tuples_grid[row + 1][col])
    if 0 < col:
        adjacent_cells.append(tuples_grid[row][col - 1])
    if col < max_col:
        adjacent_cells.append(tuples_grid[row][col + 1])
    return adjacent_cells


def build_graph(tuples_grid: list) -> nx.Graph:
    graph = nx.Graph()
    # first pass to create the nodes
    for row_num in range(len(tuples_grid)):
        for col_num in range(len(tuples_grid[row_num])):
            node = graph.add_node(tuples_grid[row_num][col_num])

    # second pass to create the edges / links
    for row_num in range(len(tuples_grid)):
        for col_num in range(len(tuples_grid[row_num])):
            n1 = tuples_grid[row_num][col_num]
            adjacents = get_adjacent_cells((row_num, col_num), tuples_grid)

            for n2 in adjacents:
                if graph.has_edge(n1, n2):
                    continue
                else:
                    r1, c1, height1 = n1
                    r2, c2, height2 = n2
                    # if ord(height2) == ord(height1) + 1 or ord(height2) == ord(height1):
                    if ord(height1)-1 <= ord(height2) and ord(height2) <= ord(height1)+1:
                        graph.add_edge(n1, n2)
    return graph
def find_edges(graph, h1, h2) -> list:
    found_edges = []
    all_edges = nx.edges(graph)
    for edge in all_edges:
        n1, n2 = edge
        r1, c1, height1 = n1
        r2, c2, height2 = n2
        if (h1 == height1 and h2 == height2) or (h1 == height2 and h2 == height1):
            found_edges.append(edge)
    return found_edges

def find_nodes(graph, h1)-> list:
    found_nodes = []
    all_nodes = nx.nodes(graph)
    for node in all_nodes:
        r, c, h = node
        if h == h1:
            found_nodes.append(node)
    return found_nodes

def parse(puzzle_input: str) -> list:
    return puzzle_input.split('\n')


def solve_part_1(data: list) -> int:
    grid = build_grid(data)
    tuples_grid = build_grid_of_tuples(grid)
    start, end = find_start_end(tuples_grid)
    graph = build_graph(tuples_grid)

    # print("edges.......")
    # edges = find_edges(graph, 'm', 'n')
    # print(edges)

    # paths = nx.shortest_path(graph, source=start)
    # path_lengths = nx.shortest_path_length(graph, source=start)
    # print(path_lengths)

    pass
    paths = nx.shortest_path(graph, source=end)
    path = nx.shortest_path(graph, source=end, target=start)
    return len(path) - 1

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

