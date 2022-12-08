import pytest
from anytree import Node


@pytest.fixture()
def data():
    with open("./day_7_data.txt") as data_file:
        data = data_file.readlines()

    return data


class Command:
    cd = False
    ls = False
    to_dir = ""

class Output:
    pass


def parse_command(line_items: list) -> Command:
    command = Command()
    if line_items[0] == "cd":
        command.cd = True
        command.to_dir = line_items[1]
    elif line_items[0] == "ls":
        command.ls = True
    else:
        assert False, f"unknown command: {line_items[0]}"

    return command


def parse_output(line_items: list) -> Output:
    output = Output()
    if line_items[0] == "dir":
        output.dir_name = line_items[1]
    elif line_items[0].isnumeric():
        output.file_size = int(line_items[0])
        output.file_name = line_items[1]
    else:
        assert False, f"unknown output: {line_items}"

    return output




def test_dir_tree(data):
    root = Node("/", parent=None)
    cur_dir = None
    command = None

    for line in data:
        line_items = line.split()
        if line_items[0] == "$":
            command = parse_command(line_items[1:])
            if command.cd:
                print(f"CD {command.to_dir}")
                if command.to_dir == "/":
                    cur_dir = root
                else:
                    pass
            elif command.ls:
                print("LS")
                pass
            else:
                assert False

        else:
            output = parse_output(line_items)


    pass


class DirNode(Node):
    pass

class FileNode(Node):
    size: int = 0


def calc_space_used(root: DirNode) -> int:
    total = 0
    for child in root.children:
        if isinstance(child, FileNode):
            total += child.size
        if isinstance(child, DirNode):
            total += calc_space_used(child)

    return total


def test_anytree():
    root = DirNode("root", parent=None)

    # build root level
    dir_a = DirNode("a", parent=root)
    file_b = FileNode("b.txt", parent=root)
    file_b.size = 14848514
    file_c = FileNode("c.txt", parent=root)
    file_c.size = 8504156
    dir_d = DirNode("d", parent=root)

    assert calc_space_used(root) == file_b.size + file_c.size

    # build dir_a
    dir_e = DirNode("e", parent=dir_a)
    file_f = FileNode("f", parent=dir_a)
    file_f.size = 29116
    file_g = FileNode("g", parent=dir_a)
    file_g.size = 2557
    file_h = FileNode("h.lst", parent=dir_a)
    file_h.size = 62596

    assert calc_space_used(dir_a) == sum([file_f.size, file_g.size, file_h.size])
    assert calc_space_used(root) == sum([file_b.size, file_c.size, file_f.size, file_g.size, file_h.size])

    # build dir_e
    file_i = FileNode("i", parent=dir_e)
    file_i.size = 584

    assert calc_space_used(dir_e) == file_i.size
    assert calc_space_used(dir_a) == sum([file_f.size, file_g.size, file_h.size, file_i.size])
    assert calc_space_used(root) == sum([file_b.size, file_c.size, file_f.size, file_g.size, file_h.size, file_i.size])

    # build dir_d
    file_j = FileNode("j", parent=dir_d)
    file_j.size = 4060174
    file_d_log = FileNode("d.log", parent=dir_d)
    file_d_log.size=8033020
    file_d_ext = FileNode("k", parent=dir_d)
    file_d_ext.size=5626152
    file_k = FileNode("k", parent=dir_d)
    file_k.size=7214296

    assert calc_space_used(dir_d) == sum([file_j.size, file_d_ext.size, file_d_log.size, file_k.size])
    assert calc_space_used(root) == 48381165





