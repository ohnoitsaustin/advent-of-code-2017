from typing import List, Tuple
from math import sqrt, ceil, floor

Grid = List[List[int]]


def rotate_list(l: List, n: int) -> List:
    return l[n:] + l[:n]


def screen_output(screen: Grid) -> str:
    return '\n'.join([''.join(str(row)) for row in screen])


def closest_square(n: int) -> int:
    return ceil(sqrt(n)) ** 2


def center_of_grid(grid: Grid) -> Tuple[int, int]:
    center_x = ceil(len(grid)/2)-1
    return center_x, center_x


def up(x: int, y: int):
    return x, y-1


def down(x: int, y: int):
    return x, y+1


def left(x: int, y: int):
    return x-1, y


def right(x: int, y: int):
    return x+1, y


def is_in_grid(grid: Grid, x: int, y: int) -> bool:
    return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)


def adjacent_values(grid: Grid, x: int, y: int) -> List[int]:
    adjacent_coords = [
        (x - 1, y-1),
        (x, y-1),
        (x + 1, y-1),
        (x - 1, y),
        (x, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]
    return [grid[y][x] for (x, y) in adjacent_coords if is_in_grid(grid, x, y)]


def fill_grid(grid: Grid, index: int) -> Tuple[int, int, int]:
    first_largest_number = 0
    x, y = center_of_grid(grid)
    i = 1
    directions = [
        right,
        up,
        left,
        down
    ]
    grid[y][x] = 1
    while i < index:
        prev_x, prev_y = x, y
        x, y = directions[0](x, y)
        if grid[y][x] != 0:
            directions = rotate_list(directions, -1)
            x, y = directions[0](prev_x, prev_y)

        directions = rotate_list(directions, 1)

        i += 1
        sum_of_adjacent_values = sum(adjacent_values(grid, x, y))
        grid[y][x] = sum_of_adjacent_values
        if first_largest_number == 0 and sum_of_adjacent_values > index:
            first_largest_number = sum_of_adjacent_values
    return x, y, first_largest_number


def make_grid(maxIndex: int) -> Grid:
    edge_size = int(sqrt(closest_square(maxIndex)))
    grid = [[0 for i in range(edge_size)] for j in range(edge_size)]

    return grid


def steps_from_center(grid: Grid, x: int, y: int) -> int:
    center_x, center_y = center_of_grid(grid)
    x_distance = abs(center_x - x)
    y_distance = abs(center_y - y)
    return x_distance + y_distance


def answer(access_point: int) -> Tuple[int, int]:
    grid = make_grid(access_point)
    x, y, first_largest_n = fill_grid(grid, access_point)
    steps = steps_from_center(grid, x, y)
    return steps, first_largest_n

puzzle_input = 361527

print(answer(1))
print(answer(2))
print(answer(10))
# print([0, 3, 2, 31])

print(answer(puzzle_input))


# (0, 0)
# (1, 0)
# (3, 11)
# (326, 363010)