import os
import re

import helpers


def get_scratchcard_points(file_path: os.path):
    return _get_scratchcard_points(file=file_path)


def _get_scratchcard_points(file: os.path) -> int:
    with open(file) as puzzle_input:
        cards = puzzle_input.readlines()
        score = 0
        for card in cards:
            pipe_card = card.replace(":", "|")
            winning_numbers = set(map(int, re.findall(r"\d+", pipe_card.split("|")[1])))
            card_numbers = set(map(int, re.findall(r"\d+", pipe_card.split("|")[2])))
            matches = len(winning_numbers.intersection(card_numbers))
            points = 2 ** (matches - 1) if matches != 0 else 0
            score += points
        return score


helpers.print_timed_results(day=1, solution_func=get_scratchcard_points)
