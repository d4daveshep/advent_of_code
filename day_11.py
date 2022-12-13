import time
from collections import deque

from aocd.models import Puzzle


def inspect_0(worry_level: int) -> (int, int):
    worry_level = (worry_level * 13) // 3
    if worry_level % 2 == 0:
        throw_to = 5
    else:
        throw_to = 2
    return worry_level, throw_to


def inspect_1(worry_level: int) -> (int, int):
    worry_level = (worry_level + 7) // 3
    if worry_level % 13 == 0:
        throw_to = 4
    else:
        throw_to = 3
    return worry_level, throw_to


def inspect_2(worry_level: int) -> (int, int):
    worry_level = (worry_level + 2) // 3
    if worry_level % 5 == 0:
        throw_to = 5
    else:
        throw_to = 1
    return worry_level, throw_to


def inspect_3(worry_level: int) -> (int, int):
    worry_level = (worry_level * 2) // 3
    if worry_level % 3 == 0:
        throw_to = 6
    else:
        throw_to = 7
    return worry_level, throw_to


def inspect_4(worry_level: int) -> (int, int):
    worry_level = (worry_level * worry_level) // 3
    if worry_level % 11 == 0:
        throw_to = 7
    else:
        throw_to = 3
    return worry_level, throw_to


def inspect_5(worry_level: int) -> (int, int):
    worry_level = (worry_level + 6) // 3
    if worry_level % 17 == 0:
        throw_to = 4
    else:
        throw_to = 1
    return worry_level, throw_to


def inspect_6(worry_level: int) -> (int, int):
    worry_level = (worry_level + 1) // 3
    if worry_level % 7 == 0:
        throw_to = 0
    else:
        throw_to = 2
    return worry_level, throw_to


def inspect_7(worry_level: int) -> (int, int):
    worry_level = (worry_level + 8) // 3
    if worry_level % 19 == 0:
        throw_to = 6
    else:
        throw_to = 0
    return worry_level, throw_to


def do_inspection(item: int, func):
    return func(item)


class Monkey:
    def __init__(self, id: int):
        self.id = id
        self.items = None
        self.inspect = None
        self.inspection_count = 0

    def starting_items(self, items: list):
        self.items = deque(items)


class KeepAway:
    def __init__(self, num_monkeys: int):
        self.num_monkeys = num_monkeys
        self.monkeys = [Monkey(i) for i in range(self.num_monkeys)]

    def do_round(self):
        for monkey in self.monkeys:
            # print(f"Monkey {monkey.id}")
            while len(monkey.items):
                worry_level = monkey.items.popleft()
                # print(f"item {worry_level}")
                new_level, throw_to = do_inspection(worry_level, monkey.inspect)
                monkey.inspection_count += 1
                # print(f"new_level {new_level}, throwing to Monkey {throw_to}")
                self.monkeys[throw_to].items.append(new_level)

    def monkey_business_score(self) -> int:
        counts = []
        for monkey in self.monkeys:
            counts.append(monkey.inspection_count)
        counts.sort(reverse=True)
        return counts[0] * counts[1]


def parse(puzzle_input: str) -> list:
    return puzzle_input.split('\n')


def solve_part_1(data: list) -> int:
    game = KeepAway(8)
    game.monkeys[0].starting_items([91, 54, 70, 61, 64, 64, 60, 85])
    game.monkeys[0].inspect = inspect_0
    game.monkeys[1].starting_items([82])
    game.monkeys[1].inspect = inspect_1
    game.monkeys[2].starting_items([84, 93, 70])
    game.monkeys[2].inspect = inspect_2
    game.monkeys[3].starting_items([78, 56, 85, 93])
    game.monkeys[3].inspect = inspect_3
    game.monkeys[4].starting_items([64, 57, 81, 95, 52, 71, 58])
    game.monkeys[4].inspect = inspect_4
    game.monkeys[5].starting_items([58, 71, 96, 58, 68, 90])
    game.monkeys[5].inspect = inspect_5
    game.monkeys[6].starting_items([56, 99, 89, 97, 81])
    game.monkeys[6].inspect = inspect_6
    game.monkeys[7].starting_items([68, 72])
    game.monkeys[7].inspect = inspect_7

    for _ in range(20):
        game.do_round()
    return game.monkey_business_score()


def solve_part_2(data: list) -> int:
    pass

if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=11)
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
