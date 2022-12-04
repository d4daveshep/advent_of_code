# day_1.py

from aocd.models import Puzzle


def parse(puzzle_input: str) -> dict:
    """Parse input."""
    dict_of_list = {}
    key = 1
    data = puzzle_input.split('\n')
    int_list = []
    for int_string in data:
        try:
            int_list.append(int(int_string))
        except ValueError:
            dict_of_list[key] = int_list.copy()
            int_list.clear()
            key += 1
    return dict_of_list


def solve_part_1(data: dict) -> int:
    # find the max number of calories carried by an elf by summing each list
    max_calories = 0
    for key, int_list in data.items():
        total_calories = sum(int_list)
        max_calories = max(max_calories, total_calories)
    return max_calories


def solve_part_2(data: dict) -> int:
    # find the sum total calories of the top 3 calorie carrying elves

    list_of_total_calories = []
    for key, int_list in data.items():
        list_of_total_calories.append(sum(int_list))

    list_of_total_calories.sort(reverse=True)  # sort biggest to smallest

    total_of_max_3 = sum(list_of_total_calories[:3])

    return total_of_max_3


if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=1)
    puzzle_input = puzzle.input_data
    data = parse(puzzle_input)

    solution_1 = solve_part_1(data)
    print(f"Part 1 solution = {solution_1}")

    solution_2 = solve_part_2(data)
    print(f"Part 2 solution = {solution_2}")


