import os

import helpers


def get_possible_games(file_path: os.path):
    possible_games = _get_possible_games(file=file_path)
    pass


def _get_possible_games(file: os.path):
    with open(file) as puzzle_input:
        lines = puzzle_input.read()
        print(lines)


helpers.print_timed_results(day=2, solution_func=get_possible_games)
