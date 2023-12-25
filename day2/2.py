import os
import re

import helpers


def get_minimum_cube_powers(file_path: os.path):
    powers = _get_powers(file=file_path)
    return sum(powers)


def _get_powers(file: os.path):
    with open(file) as puzzle_input:
        lines = puzzle_input.readlines()
        powers = []
        for line in lines:
            cubes = line.strip().split(":")[1]
            all_red = re.findall(r"\d+ red", cubes)
            all_green = re.findall(r"\d+ green", cubes)
            all_blue = re.findall(r"\d+ blue", cubes)
            highest_red = _find_highest_for_colour(cubes_by_colour=all_red)
            highest_green = _find_highest_for_colour(cubes_by_colour=all_green)
            highest_blue = _find_highest_for_colour(cubes_by_colour=all_blue)
            powers.append(highest_red * highest_green * highest_blue)
        return powers


def _find_highest_for_colour(cubes_by_colour: list[str]) -> int:
    return max([int(entry.split()[0]) for entry in cubes_by_colour])


helpers.print_timed_results(solution_func=get_minimum_cube_powers)
