from collections import deque


def do_inspection(item: int, func):
    return func(item)


class Monkey:
    def __init__(self, id: int):
        self.id = id
        self.items = None
        self.inspect = None
        self.inspection_count = 0

    def starting_items(self, items:list):
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




