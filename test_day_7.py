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



