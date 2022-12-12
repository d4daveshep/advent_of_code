import time

from aocd.models import Puzzle


class Program:
    def __init__(self):
        self.__x = 1
        self.cycles = 0
        self.end_of_cycle_history = {self.cycles:self.__x}

    def process_instruction(self, instruction):
        data = instruction.strip().split()
        if data[0] == "noop":
            self.cycles += 1
            self.end_of_cycle_history[self.cycles] = self.__x
        elif data[0] == "addx":
            self.cycles += 1
            self.end_of_cycle_history[self.cycles] = self.__x
            self.cycles += 1
            self.__x += int(data[1])
            self.end_of_cycle_history[self.cycles] = self.__x

        else:
            raise Exception(f"invalid operation: {data[0]}")

    def process_instructions(self, instructions: list):
        for line in instructions:
            self.process_instruction(line)

    def signal_strength_during_cycle(self, cycle: int) -> int:
        return self.x_during_cycle(cycle) * cycle

    def sum_signal_strength(self):
        total = 0
        for cycle in range(20, 240, 40):
            total += self.signal_strength_during_cycle(cycle)
        return total

    def x_during_cycle(self, cycle:int) -> int:
        return self.end_of_cycle_history[cycle-1]

    def x_after_cycle(self, cycle:int) -> int:
        return self.end_of_cycle_history[cycle]


def parse(puzzle_input: str) -> list:
    return puzzle_input.split('\n')


def solve_part_1(data: list) -> int:
    program = Program()
    program.process_instructions(data)
    return program.sum_signal_strength()

def solve_part_2(data: list) -> int:
    pass


if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=10)
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
