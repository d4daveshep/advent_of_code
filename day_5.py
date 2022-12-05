from collections import deque

from aocd.models import Puzzle

def parse(puzzle_input: str) -> list:
    return puzzle_input.split('\n')



def parse_stacks(puzzle_input: str) -> list:
    first_rows = puzzle_input.split('\n')[:8]
    first_rows.reverse()

    stacks = []
    for _ in range(9):
        stacks.append(deque())

    for row in first_rows:
        for i in range(9):
            char = row[1 + i*4]
            if char.isalnum():
                stacks[i].append(char)

    return stacks


def parse_moves(puzzle_input):
    moves = puzzle_input.split('\n')[10:]
    return moves

def do_move_for_part_1(stacks:list, move_str:str):
    words = move_str.split()
    num_to_move = int(words[1])
    from_stack = int(words[3])
    to_stack = int(words[5])

    for _ in range(num_to_move):
        crate = stacks[from_stack-1].pop()
        stacks[to_stack-1].append(crate)

def do_move_for_part_2(stacks:list, move_str:str):
    words = move_str.split()
    num_to_move = int(words[1])
    from_stack = int(words[3])
    to_stack = int(words[5])

    crates = deque()
    for _ in range(num_to_move):
        crate = stacks[from_stack-1].pop()
        crates.appendleft(crate)

    stacks[to_stack-1].extend(crates)


def get_final_state(final_stacks) -> str:
    final_state = ""
    for stack in final_stacks:
        final_state += stack.pop()

    return final_state

def solve_part_1(inital_stacks: list, moves: list) -> str:
    stacks = inital_stacks
    for move in moves:
        do_move_for_part_1(stacks, move)

    final_state = get_final_state(stacks)
    return final_state



def solve_part_2(inital_stacks: list, moves: list) -> str:
    stacks = inital_stacks
    for move in moves:
        do_move_for_part_2(stacks, move)

    final_state = get_final_state(stacks)
    return final_state



if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=5)
    puzzle_input = puzzle.input_data

    stacks = parse_stacks(puzzle_input)
    moves = parse_moves(puzzle_input)

    part_1_answer = solve_part_1(stacks, moves)
    print(f"Part 1 answer = {part_1_answer}")

    stacks = parse_stacks(puzzle_input)
    moves = parse_moves(puzzle_input)

    part_2_answer = solve_part_2(stacks, moves)
    print(f"Part 2 answer = {part_2_answer}")
