from collections import Counter

from aocd.models import Puzzle


def find_first_marker(data):
    for i in range(len(data)-4):
        test_marker = data[i:i+4]
        assert len(test_marker) == 4
        counter = Counter(test_marker)
        if len(counter) == 4:
            return i+4

def find_message_marker(data):
    for i in range(len(data)-14):
        test_marker = data[i:i+14]
        assert len(test_marker) == 14
        counter = Counter(test_marker)
        if len(counter) == 14:
            return i+14


def parse(puzzle_input: str) -> list:
    return puzzle_input.split('\n')


def solve_part_1(data: str) -> int:
    return find_first_marker(data)


def solve_part_2(data: str) -> int:
    return find_message_marker(data)


if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=6)
    puzzle_input = puzzle.input_data


    part_1_answer = solve_part_1(puzzle_input)
    print(f"Part 1 answer = {part_1_answer}")

    part_2_answer = solve_part_2(puzzle_input)
    print(f"Part 2 answer = {part_2_answer}")
