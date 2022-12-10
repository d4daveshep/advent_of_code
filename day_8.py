import time

import pandas as pd
from aocd.models import Puzzle


def convert_string_to_list_of_ints(data_string: str) -> list:
    ints = []
    for s in data_string:
        ints.append(int(s))
    return ints


def build_dataframe(data: list) -> pd.DataFrame:
    index = [i for i in range(len(data))]
    df = pd.DataFrame(columns=index, index=index)
    row_count = 0
    for line in data:
        ints = convert_string_to_list_of_ints(line.strip())
        df.loc[row_count] = ints
        row_count += 1
    return df


def calc_perimeter_length(df):
    size = df.shape[0]
    perimeter_length = size * 4 - 4
    return perimeter_length


def north_visibility(df: pd.DataFrame, loc: tuple) -> bool:
    i, j = loc
    cell = df[j][i]
    col = df[j].tolist()
    max_to_edge = max(col[:i])
    visible = cell > max_to_edge
    return visible


def calc_trees_visible_north(df: pd.DataFrame, loc: tuple) -> int:
    i, j = loc
    cell = df[j][i]
    col = df[j].tolist()
    counter = 0
    for k in col[i - 1::-1]:
        if k < cell:
            counter += 1
        if k >= cell:
            counter += 1
            break
    return counter


def calc_trees_visible_west(df: pd.DataFrame, loc: tuple) -> int:
    i, j = loc
    cell = df[j][i]
    row = df.loc[i].tolist()
    counter = 0
    for k in row[j - 1::-1]:
        if k < cell:
            counter += 1
        if k >= cell:
            counter += 1
            break
    return counter


def calc_trees_visible_east(df: pd.DataFrame, loc: tuple) -> int:
    i, j = loc
    cell = df[j][i]
    row = df.loc[i].tolist()
    counter = 0
    for k in row[j + 1:]:
        if k < cell:
            counter += 1
        if k >= cell:
            counter += 1
            break
    return counter


def calc_trees_visible_south(df: pd.DataFrame, loc: tuple) -> int:
    i, j = loc
    cell = df[j][i]
    col = df[j].tolist()
    counter = 0
    for k in col[i + 1:]:
        if k < cell:
            counter += 1
        if k >= cell:
            counter += 1
            break
    return counter


def south_visibility(df: pd.DataFrame, loc: tuple) -> bool:
    i, j = loc
    cell = df[j][i]
    col = df[j].tolist()
    max_to_edge = max(col[i + 1:])
    visible = cell > max_to_edge
    return visible


def west_visibility(df: pd.DataFrame, loc: tuple) -> bool:
    i, j = loc
    cell = df[j][i]
    row = df.loc[i].tolist()
    max_to_edge = max(row[:j])
    visible = cell > max_to_edge
    return visible


def east_visibility(df: pd.DataFrame, loc: tuple) -> bool:
    i, j = loc
    cell = df[j][i]
    row = df.loc[i].tolist()
    max_to_edge = max(row[j + 1:])
    visible = cell > max_to_edge
    return visible


def calc_visibility_of_internal_cells(df) -> int:
    counter = 0
    size = df.shape[0]
    for i in range(1, size - 1):
        for j in range(1, size - 1):
            cell = df[j][i]
            if north_visibility(df, (i, j)) \
                    or south_visibility(df, (i, j)) \
                    or west_visibility(df, (i, j)) \
                    or east_visibility(df, (i, j)):
                counter += 1
    return counter


def calc_total_visible_cells(df):
    return calc_perimeter_length(df) + calc_visibility_of_internal_cells(df)


def calc_scenic_score(df: pd.DataFrame, loc: tuple) -> int:
    i,j = loc
    score = 1
    size = df.shape[0]
    cell = df[j][i]
    score *= (calc_trees_visible_north(df, (i, j)) *
              calc_trees_visible_south(df,(i, j)) *
              calc_trees_visible_west(df, (i, j)) *
              calc_trees_visible_east(df, (i, j)))
    return score


def parse(puzzle_input: str) -> list:
    return puzzle_input.split('\n')


def solve_part_1(df: pd.DataFrame) -> int:
    return calc_total_visible_cells(df)


def solve_part_2(df: pd.DataFrame) -> int:
    max_score = 0
    size = df.shape[0]
    for i in range(size):
        for j in range(size):
            max_score = max([max_score, calc_scenic_score(df, (i,j))])
    return max_score



if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=8)
    puzzle_input = puzzle.input_data
    data = parse(puzzle_input)
    df = build_dataframe(data)

    tic = time.perf_counter()
    part_1_answer = solve_part_1(df)
    toc = time.perf_counter()
    print(f"Part 1 answer = {part_1_answer}")
    print(f"took {(toc - tic) * 1000:0.1f} msec")

    tic = time.perf_counter()
    part_2_answer = solve_part_2(df)
    toc = time.perf_counter()
    print(f"Part 2 answer = {part_2_answer}")
    print(f"took {(toc - tic) * 1000:0.1f} msec")
