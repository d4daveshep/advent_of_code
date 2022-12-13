from collections import deque

from day_11 import Monkey, KeepAway, do_inspection


def inspect_0(worry_level: int) -> (int, int):
    worry_level = (worry_level * 19) // 3
    if worry_level % 23 == 0:
        throw_to = 2
    else:
        throw_to = 3
    return worry_level, throw_to


def inspect_1(worry_level: int) -> (int, int):
    worry_level = (worry_level + 6) // 3
    if worry_level % 19 == 0:
        throw_to = 2
    else:
        throw_to = 0
    return worry_level, throw_to


def inspect_2(worry_level: int) -> (int, int):
    worry_level = (worry_level * worry_level) // 3
    if worry_level % 13 == 0:
        throw_to = 1
    else:
        throw_to = 3
    return worry_level, throw_to


def inspect_3(worry_level: int) -> (int, int):
    worry_level = (worry_level + 3) // 3
    if worry_level % 17 == 0:
        throw_to = 0
    else:
        throw_to = 1
    return worry_level, throw_to


def test_monkey():
    monkey = Monkey(0)
    monkey.starting_items([79, 98])

    worry, new_monkey = do_inspection(monkey.items[0], inspect_0)
    assert worry == 500
    assert new_monkey == 3
    worry, new_monkey = do_inspection(monkey.items[1], inspect_0)
    assert worry == 620
    assert new_monkey == 3


def test_game():
    game = KeepAway(4)
    game.monkeys[0].starting_items([79, 98])
    game.monkeys[0].inspect = inspect_0

    game.monkeys[1].starting_items([54, 65, 75, 74])
    game.monkeys[1].inspect = inspect_1

    game.monkeys[2].starting_items([79, 60, 97])
    game.monkeys[2].inspect = inspect_2

    game.monkeys[3].starting_items([74])
    game.monkeys[3].inspect = inspect_3

    game.do_round()
    assert game.monkeys[0].items == deque([20, 23, 27, 26])
    assert game.monkeys[1].items == deque([2080, 25, 167, 207, 401, 1046])
    assert game.monkeys[2].items == deque([])
    assert game.monkeys[3].items == deque([])

    game.do_round()
    assert game.monkeys[0].items == deque([695, 10, 71, 135, 350])
    assert game.monkeys[1].items == deque([43, 49, 58, 55, 362])
    assert game.monkeys[2].items == deque([])
    assert game.monkeys[3].items == deque([])

    for _ in range(18):
        game.do_round()
    assert game.monkeys[0].items == deque([10, 12, 14, 26, 34])
    assert game.monkeys[1].items == deque([245, 93, 53, 199, 115])
    assert game.monkeys[2].items == deque([])
    assert game.monkeys[3].items == deque([])

    assert game.monkeys[0].inspection_count == 101
    assert game.monkeys[1].inspection_count == 95
    assert game.monkeys[2].inspection_count == 7
    assert game.monkeys[3].inspection_count == 105

    assert game.monkey_business_score() == 10605

