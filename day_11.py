from collections import deque


def do_inspection(item: int, func):
    return func(item)


class Monkey:
    def __init__(self, id: int):
        self.items = None
        self.inspect = None

    def starting_items(self, items:list):
        self.items = deque(items)



class KeepAway:
    def __init__(self, num_monkeys: int):
        self.num_monkeys = num_monkeys
        self.monkeys = [Monkey(i) for i in range(self.num_monkeys)]

    def do_round(self):
        pass
