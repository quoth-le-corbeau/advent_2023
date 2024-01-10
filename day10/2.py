import os

import helpers


def RENAME_FUNC(file_path: os.path):
    RENAME = _RENAME_FUNC(file=file_path)
    pass


def _RENAME_FUNC(file: os.path):
    with open(file) as puzzle_input:
        lines = puzzle_input.read()
        print(lines)


helpers.print_timed_results(solution_func=RENAME_FUNC)
