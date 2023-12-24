import os

import helpers


def find_part_numbers(file_path: os.path):
    all_part_numbers = _get_part_numbers(file=file_path)
    pass


def _get_part_numbers(file: os.path):
    with open(file) as puzzle_input:
        grid = puzzle_input.readlines()
        part_number_coordinates: list[tuple] = list()
        for row_index, row in enumerate(grid):
            row = row.strip()
            for index, column in enumerate(row):
                if not (column.isdigit() or column == ".") and 1 < index < len(row) - 1:
                    for local_grid_row in [
                        grid[row_index - 1],
                        grid[row_index],
                        grid[row_index + 1],
                    ]:
                        local_grid_row = local_grid_row.strip()
                        for local_grid_point in [
                            local_grid_row[index - 1],
                            local_grid_row[index],
                            local_grid_row[index + 1],
                        ]:
                            if local_grid_point.isdigit():
                                print(local_grid_point)
        print(f"{part_number_coordinates=}")


helpers.print_timed_results(day=1, solution_func=find_part_numbers)
