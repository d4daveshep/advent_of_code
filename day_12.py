import networkx as nx


def build_grid(lines: list) -> list:
    grid = []
    for line in lines:
        row = list(line.strip())
        grid.append(row)
    return grid


def build_grid_of_tuples(grid) -> list:
    for row_num in range(len(grid)):
        for col_num in range(len(grid[row_num])):
            height = grid[row_num][col_num]
            if height == "S":
                height = chr(ord("a") - 1)
            elif height == "E":
                height = chr(ord("z") + 1)

            grid[row_num][col_num] = (row_num, col_num, height)
    return grid


def get_adjacent_cells(row_col: tuple, tuples_grid: list) -> list:
    row, col = row_col
    max_row = len(tuples_grid) - 1
    max_col = len(tuples_grid[0]) - 1
    adjacent_cells = []
    if 0 < row:
        adjacent_cells.append(tuples_grid[row - 1][col])
    if row < max_row:
        adjacent_cells.append(tuples_grid[row + 1][col])
    if 0 < col:
        adjacent_cells.append(tuples_grid[row][col - 1])
    if col < max_col:
        adjacent_cells.append(tuples_grid[row][col + 1])
    return adjacent_cells


def build_graph(tuples_grid: list) -> nx.Graph:
    graph = nx.Graph()
    # first pass to create the nodes
    for row_num in range(len(tuples_grid)):
        for col_num in range(len(tuples_grid[row_num])):
            node = graph.add_node(tuples_grid[row_num][col_num])

    # second pass to create the edges / links
    for row_num in range(len(tuples_grid)):
        for col_num in range(len(tuples_grid[row_num])):
            n1 = tuples_grid[row_num][col_num]
            adjacents = get_adjacent_cells((row_num, col_num), tuples_grid)

            for n2 in adjacents:
                if graph.has_edge(n1, n2):
                    continue
                else:
                    r1, c1, height1 = n1
                    r2, c2, height2 = n2
                    if height2 > height1:
                        graph.add_edge(n1, n2)

    return graph
