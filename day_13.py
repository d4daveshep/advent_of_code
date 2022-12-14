# alternate solution for Day 12 using my own Graph structure
import time
from collections import deque
from functools import cmp_to_key
from itertools import zip_longest

from aocd.models import Puzzle


def parse_data_pairs(test_data):
    data_deque = deque(test_data)
    data_pairs = []
    while len(data_deque):
        left = eval(data_deque.popleft())
        right = eval(data_deque.popleft())
        data_pairs.append((left, right))
        try:
            blank = data_deque.popleft()
        except IndexError:
            pass
    return data_pairs

def parse_data(raw_data):
    parsed_data = []
    for line in raw_data:
        if len(line.strip()):
            parsed_data.append(eval(line))
    return parsed_data


def compare(left, right) -> int:
    """
    Borrowed this solution.  it uses a few things i wouldn't normally use like walrus operator, zip function, ternery statements
    :param left: int or list or None
    :param right: int or list or None
    :return: -1 if left < right, +1 if left > right or 0 if left == right
    """
    # left or right could be None from zip_longest
    if left is None:
        return -1
    if right is None:
        return 1

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0

    elif isinstance(left, list) and isinstance(right, list):
        for l2, r2 in zip_longest(left, right):
            if (result := compare(l2, r2)) != 0:
                return result
        return 0

    else:
        l2 = [left] if isinstance(left, int) else left
        r2 = [right] if isinstance(right, int) else right
        return compare(l2, r2)


def parse(puzzle_input: str) -> list:
    return puzzle_input.split('\n')


def solve_part_1(data: list) -> int:
    data_pairs = parse_data_pairs(data)
    sum_total = 0
    for i in range(len(data_pairs)):
        left, right = data_pairs[i]
        answer = compare(left, right)
        if answer == -1:
            sum_total += i + 1
    return sum_total


def solve_part_2(data: list) -> int:
    '''
    Strategy to solve is as follows
    read the data into a list ignoring blank rows and original ordering
    Add the additional packets [2] and [6]
    TODO Use the compare function as the key= from part 1 as the sorting algorithm
    then find the location of where [2] nad [6] are.
    Add them together to get the answer
    :param data:
    :return:
    '''
    data = parse_data(data)
    data.append([[2]])
    data.append([[6]])
    sorted_data = sorted(data, key=cmp_to_key(compare))
    index_2 = sorted_data.index([[2]]) + 1
    index_6 = sorted_data.index([[6]]) + 1

    return index_2 * index_6


if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=13)
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
