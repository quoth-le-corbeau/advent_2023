import os
import re

import helpers


def get_possible_games(file_path: os.path):
    possible_games = _get_possible_games(file=file_path)
    return sum(possible_games)


def _get_possible_games(file: os.path):
    with open(file) as puzzle_input:
        lines = puzzle_input.readlines()
        possible = []
        for line in lines:
            game_number = int(re.findall(r"Game \d+", line.strip())[0].split()[1])
            cubes = line.strip().split(":")[1]
            all_red = re.findall(r"\d+ red", cubes)
            all_green = re.findall(r"\d+ green", cubes)
            all_blue = re.findall(r"\d+ blue", cubes)
            impossible_red = _is_game_impossible(
                cubes_by_colour=all_red, max_for_colour=12
            )
            impossible_green = _is_game_impossible(
                cubes_by_colour=all_green, max_for_colour=13
            )
            impossible_blue = _is_game_impossible(
                cubes_by_colour=all_blue, max_for_colour=14
            )
            if any([impossible_red, impossible_green, impossible_blue]):
                continue
            else:
                possible.append(game_number)
        return possible


def _is_game_impossible(cubes_by_colour: list[str], max_for_colour: int):
    return any(int(entry.split()[0]) > max_for_colour for entry in cubes_by_colour)


helpers.print_timed_results(day=2, solution_func=get_possible_games)
