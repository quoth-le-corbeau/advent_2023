import math
import os

import helpers


def find_winners_product(file_path: os.path):
    game = _parse_games(file=file_path)
    return _find_winning_combinations(game=game)


def _find_winning_combinations(game: tuple[int, int]) -> int:
    time, distance = game
    discriminant = time**2 - (4 * distance)
    lower_root = math.floor((time - math.sqrt(discriminant)) / 2)
    upper_root = math.ceil((time + math.sqrt(discriminant)) / 2)
    return upper_root - lower_root - 1


def _parse_games(file: os.path) -> tuple[int, int]:
    with open(file) as puzzle_input:
        time_line = puzzle_input.readline()
        time = "".join(time_line.split(":")[1].strip().split())
        distance_line = puzzle_input.readline()
        distance = "".join(distance_line.split(":")[1].strip().split())
        return int(time), int(distance)


helpers.print_timed_results(solution_func=find_winners_product)
