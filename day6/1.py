import functools
import math
import os
import helpers


def find_winners_product(file_path: os.path):
    games = _parse_games(file=file_path)
    ways_to_win = list()
    for game in games:
        ways_to_win.append(_find_winning_combinations(game=game))
    return functools.reduce(int.__mul__, ways_to_win)


def _find_winning_combinations(game: tuple[int, int]) -> int:
    time, distance = game
    discriminant = time**2 - (4 * distance)
    lower_root = math.floor((time - math.sqrt(discriminant)) / 2)
    upper_root = math.ceil((time + math.sqrt(discriminant)) / 2)
    return upper_root - lower_root - 1


def _parse_games(file: os.path) -> list[tuple[int, int]]:
    with open(file) as puzzle_input:
        time_line = puzzle_input.readline()
        times = list(map(int, time_line.split(":")[1].strip().split()))
        distance_line = puzzle_input.readline()
        distances = list(map(int, distance_line.split(":")[1].strip().split()))
        return list(zip(times, distances))


helpers.print_timed_results(solution_func=find_winners_product)
