from collections import Counter

from aocd.models import Puzzle


def parse(puzzle_input: str) -> list:
    return puzzle_input.split('\n')


def priority(char: str) -> int:
    assert len(char) == 1

    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38


def duplicate_char(contents: str) -> str:
    assert len(contents) % 2 == 0
    first_half, second_half = contents[:len(contents) // 2], contents[len(contents) // 2:]

    for char in first_half:
        if char in second_half:
            return char

    assert False


def solve_part_1(data: list) -> int:
    sum_of_priorities = 0

    for contents in data:
        sum_of_priorities += priority(duplicate_char(contents))

    return sum_of_priorities

def find_badge(str_1:str, str_2:str, str_3:str) -> str:
    counter_1 = Counter(str_1)
    counter_2 = Counter(str_2)
    counter_3 = Counter(str_3)

    key_counter = Counter(counter_1.keys()) #, counter_2.keys(), counter_3.keys()])
    key_counter.update(counter_2.keys())
    key_counter.update(counter_3.keys())

    unique = key_counter.most_common(1)[0][0]
    return unique

def solve_part_2(data: list) -> int:
    sum_of_priorities = 0

    assert len(data) % 3 == 0


    for i in range(0,len(data),3):
        badge = find_badge(data[i],data[i+1],data[i+2])
        sum_of_priorities += priority(badge)

    return sum_of_priorities







if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=3)
    puzzle_input = puzzle.input_data

    data = parse(puzzle_input)

    part_1_answer = solve_part_1(data)
    print(f"Part 1 answer = {part_1_answer}")

    part_2_answer = solve_part_2(data)
    print(f"Part 2 answer = {part_2_answer}")



