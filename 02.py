from typing import List
from typing import Callable


def get_rows(spreadsheet: str) -> List[str]:
    return spreadsheet.split("\n")


def get_cols(row: str) -> List[int]:
    return [int(col) for col in row.split("\t")]


def diff_of_min_and_max(values: List[int]) -> int:
    return max(values) - min(values)


def division_of_evenly_divisible_values(values: List[int]) -> int:
    for value in values:
        for other_value in values:
            if value != other_value and value % other_value == 0:
                return int(value / other_value)


def get_answer(puzzle_input: str, row_value_func: Callable[[List[int]], int]) -> str:
    rows = get_rows(puzzle_input)
    sum_of_row_values = 0
    for row in rows:
        cols = get_cols(row)
        row_value = row_value_func(cols)
        sum_of_row_values += row_value

    return sum_of_row_values


puzzleInput = open('02-input.txt', 'r').read()

answer = get_answer(puzzleInput, diff_of_min_and_max)
print('Day 2 answer 1: ' + str(answer))

answer = get_answer(puzzleInput, division_of_evenly_divisible_values)
print('Day 2 answer 2: ' + str(answer))
