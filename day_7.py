import time

from anytree import PreOrderIter, Node
from aocd.models import Puzzle


class DirNode(Node):
    def find(self, sub_dir: str) -> Node:
        for child in self.children:
            if isinstance(child, DirNode) and child.name == sub_dir:
                return child

        else:
            raise Exception(f"can't find sub-dir '{sub_dir}' in {self.children}")


class FileNode(Node):
    size: int = 0


class Command:
    def __init__(self):
        self.cd = False
        self.ls = False
        self.cd_up = False
        self.to_dir = ""


class Output:
    def __init__(self):
        self.name = ""
        self.dir = False
        self.file = False
        self.size = 0



def parse(puzzle_input: str) -> list:
    return puzzle_input.split('\n')


def parse_command(line_items: list) -> Command:
    command = Command()
    if line_items[0] == "cd":
        command.cd = True
        command.to_dir = line_items[1]
        if command.to_dir == "..":
            command.cd_up = True
    elif line_items[0] == "ls":
        command.ls = True
    else:
        assert False, f"unknown command: {line_items[0]}"

    return command


def parse_output(line_items: list) -> Output:
    output = Output()
    if line_items[0] == "dir":
        output.dir = True
        output.name = line_items[1]
    elif line_items[0].isnumeric():
        output.file = True
        output.size = int(line_items[0])
        output.name = line_items[1]
    else:
        assert False, f"unknown output: {line_items}"

    return output


def parse_line(line: str):
    obj = None
    line_items = line.split()
    if line_items[0] == "$":
        obj = parse_command(line_items[1:])
    else:
        obj = parse_output(line_items)

    return obj


def calc_space_used(root: DirNode) -> int:
    total = 0
    for child in root.children:
        if isinstance(child, FileNode):
            total += child.size
        if isinstance(child, DirNode):
            total += calc_space_used(child)

    return total


def build_tree(data):
    root_node = None
    cur_dir = None
    line_counter = 0
    for line in data:
        # line_counter += 1
        # print(f"line {line_counter}: {line}")
        obj = parse_line(line)
        if isinstance(obj, Command):
            if obj.cd:
                if obj.cd_up:
                    cur_dir = cur_dir.parent
                elif obj.to_dir == "/":
                    root_node = DirNode(obj.to_dir)
                    cur_dir = root_node
                else:
                    cur_dir = cur_dir.find(obj.to_dir)
            elif obj.ls:
                pass
        elif isinstance(obj, Output):
            if obj.dir:
                new_dir = DirNode(obj.name, parent=cur_dir)
            elif obj.file:
                new_file = FileNode(obj.name, parent=cur_dir)
                new_file.size = obj.size

    return root_node


def calc_total_dir_space_under_100k(root_node: DirNode) -> int:
    total = 0
    for node in PreOrderIter(root_node):
        if isinstance(node, DirNode):
            space = calc_space_used(node)
            if space <= 100000:
                total += space
    return total


def solve_part_1(data: str) -> int:
    root_node = build_tree(data)
    total = calc_total_dir_space_under_100k(root_node)
    return total


def calc_space_to_free(root_node):
    total_space_available = 70000000
    space_used = calc_space_used(root_node)
    unused_space = total_space_available - space_used
    space_to_find = 30000000 - unused_space

    smallest_space = 30000000
    for node in PreOrderIter(root_node):
        if isinstance(node, DirNode):
            space = calc_space_used(node)
            if space > space_to_find:
                smallest_space = min([space, smallest_space])

    return smallest_space


def solve_part_2(data: str) -> int:
    root_node = build_tree(data)
    smallest_space = calc_space_to_free(root_node)
    return smallest_space



    # return find_message_marker(data)


if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=7)
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
