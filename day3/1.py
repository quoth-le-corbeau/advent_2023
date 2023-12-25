import os

import helpers


def find_part_numbers(file_path: os.path):
    return sum(_get_all_part_numbers(file=file_path))


def _get_all_part_numbers(file: os.path) -> list[int]:
    with open(file) as puzzle_input:
        grid = puzzle_input.readlines()
        part_number_start_coordinates: set[tuple] = set()
        for row_index, row in enumerate(grid):
            row = row.strip()
            for index, column in enumerate(row):
                if not (column.isdigit() or column == ".") and 0 < index < len(row) - 1:
                    for vertical_index in [
                        row_index - 1,
                        row_index,
                        row_index + 1,
                    ]:
                        for horizontal_index in [
                            index - 1,
                            index,
                            index + 1,
                        ]:
                            if grid[vertical_index][horizontal_index].isdigit():
                                i = horizontal_index
                                while grid[vertical_index][i].isdigit() and i >= 0:
                                    i -= 1
                                part_number_start_coordinates.add(
                                    (vertical_index, i + 1)
                                )
        all_part_numbers = list()
        for coordinate in part_number_start_coordinates:
            row, column = coordinate
            part_number_string = ""
            while grid[row][column].isdigit():
                part_number_string += grid[row][column]
                column += 1
            all_part_numbers.append(int(part_number_string))
        return all_part_numbers


helpers.print_timed_results(day=1, solution_func=find_part_numbers)
