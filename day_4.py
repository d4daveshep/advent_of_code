from aocd.models import Puzzle


class Section:
    def __init__(self, section: str):
        self.start, self.end = section.split("-")
        self.start = int(self.start)
        self.end = int(self.end)

    def contains(self, obj) -> bool:
        return obj.start >= self.start and obj.end <= self.end

    def overlaps(self, obj) -> bool:
        return obj.start <= self.end and obj.end >= self.start



def parse(puzzle_input: str) -> list:
    return puzzle_input.split('\n')


def solve_part_1(data: list) -> int:
    count = 0
    for pair in data:
        str1, str2 = pair.split(",")
        section1 = Section(str1)
        section2 = Section(str2)
        if section1.contains(section2) or section2.contains(section1):
            count += 1

    return count


def solve_part_2(data: list) -> int:
    count = 0
    for pair in data:
        str1, str2 = pair.split(",")
        section1 = Section(str1)
        section2 = Section(str2)
        if section1.overlaps(section2):
            count += 1

    return count


if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=4)
    puzzle_input = puzzle.input_data

    data = parse(puzzle_input)

    part_1_answer = solve_part_1(data)
    print(f"Part 1 answer = {part_1_answer}")

    part_2_answer = solve_part_2(data)
    print(f"Part 2 answer = {part_2_answer}")
