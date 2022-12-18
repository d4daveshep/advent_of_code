# alternate solution for Day 12 using my own Graph structure
import time

from aocd.models import Puzzle


class Node:
    def __init__(self, row: int, col: int, label: str):
        self.row = row
        self.col = col
        self.label = label
        self.visited = False
        self.step = None

    def __repr__(self):
        return f"Node(row={self.row},col={self.col},label='{self.label}')"

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col and self.label == other.label

    def can_move_to(self, other):
        return ord(self.label) >= ord(other.label) - 1
        # return ord(self.label) == ord(other.label) or ord(self.label) == ord(other.label) - 1


def build_grid(lines: list) -> list:
    grid = []
    for line in lines:
        row = list(line.strip())
        grid.append(row)
    return grid


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


def find_start_end(nodes_grid) -> tuple:
    start = None
    end = None
    for row_num in range(len(nodes_grid)):
        for col_num in range(len(nodes_grid[row_num])):
            node = nodes_grid[row_num][col_num]
            height = node.label
            if height == '`':
                start = node
                continue
            if height == '{':
                end = node
                continue
            if start and end:
                break

    return start, end


def find_nodes_at_step(nodes_grid: list, step: int) -> list:
    nodes = []
    for row in nodes_grid:
        for node in row:
            if node.step == step:
                nodes.append(node)
    return nodes


def find_valid_unvisited_adjacents(nodes_grid, node) -> list:
    row = node.row
    col = node.col

    max_row = len(nodes_grid) - 1
    max_col = len(nodes_grid[0]) - 1

    adjacent_nodes = []
    if 0 < row:
        adjacent_node = nodes_grid[row - 1][col]
        if not adjacent_node.visited and node.can_move_to(adjacent_node):
            adjacent_nodes.append(adjacent_node)
    if row < max_row:
        adjacent_node = nodes_grid[row + 1][col]
        if not adjacent_node.visited and node.can_move_to(adjacent_node):
            adjacent_nodes.append(adjacent_node)
    if 0 < col:
        adjacent_node = nodes_grid[row][col - 1]
        if not adjacent_node.visited and node.can_move_to(adjacent_node):
            adjacent_nodes.append(adjacent_node)
    if col < max_col:
        adjacent_node = nodes_grid[row][col + 1]
        if not adjacent_node.visited and node.can_move_to(adjacent_node):
            adjacent_nodes.append(adjacent_node)

    return adjacent_nodes


def do_next_step(nodes_grid, step: int):
    nodes_at_current_step = find_nodes_at_step(nodes_grid, step)
    new_step = step + 1
    for node in nodes_at_current_step:
        adjacent_nodes = find_valid_unvisited_adjacents(nodes_grid, node)
        for adj_node in adjacent_nodes:
            adj_node.visited = True
            adj_node.step = new_step


def print_graph(nodes_grid):
    print()
    for row in nodes_grid:
        for node in row:
            if node.step is not None:
                print(f"{node.step:4d}{node.label}", end="")
            else:
                print(f"   .{node.label}", end="")
        print()
    pass

def find_nodes_with_label(nodes_grid:list, label:str)-> list:
    nodes_found = []
    for row in nodes_grid:
        for node in row:
            if node.label == label:
                nodes_found.append(node)
    return nodes_found


def parse(puzzle_input: str) -> list:
    return puzzle_input.split('\n')


def solve_part_1(data: list) -> int:
    grid = build_grid(data)
    nodes_grid = build_grid_of_nodes(grid)
    start, end = find_start_end(nodes_grid)
    start.step = 0
    end.step = -1
    start.visited = True

    # print_graph(nodes_grid)

    step_num = 0
    while end.step == -1:
        print(f"step: {step_num}")
        do_next_step(nodes_grid, step_num)
        step_num += 1
        # if step_num % 20 == 0:
        #     print_graph(nodes_grid)
        #     input("enter to continue")

    # print_graph(nodes_grid)

    return end.step


def solve_part_2(data: list) -> int:
    grid = build_grid(data)
    nodes_grid = build_grid_of_nodes(grid)
    start, end = find_start_end(nodes_grid)
    start.step = 0
    end.step = -1
    start.visited = True

    nodes_a = find_nodes_with_label(nodes_grid,'a')
    for node in nodes_a:
        node.step = 0
        node.visited = True

    step_num = 0
    while end.step == -1:
        print(f"step: {step_num}")
        do_next_step(nodes_grid, step_num)
        step_num += 1
        # if step_num % 20 == 0:
        #     print_graph(nodes_grid)
        #     input("enter to continue")

    # print_graph(nodes_grid)

    return end.step


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
