import os
import re
import helpers


def get_total_scratchcards(file_path: os.path):
    all_cards_won = _get_scratchcard_copies(file=file_path)
    total = 0
    for card, copies in all_cards_won.items():
        total += copies
    return total


def _get_scratchcard_copies(file: os.path):
    with open(file) as puzzle_input:
        cards = puzzle_input.readlines()
        card_copies = {i + 1: 1 for i in range(len(cards))}
        for index, card in enumerate(cards):
            current_number_of_copies = card_copies[index + 1]
            pipe_card = card.replace(":", "|")
            winning_numbers = set(map(int, re.findall(r"\d+", pipe_card.split("|")[1])))
            card_numbers = set(map(int, re.findall(r"\d+", pipe_card.split("|")[2])))
            matches = len(winning_numbers.intersection(card_numbers))
            if matches > 0:
                for i in range(1, matches + 1):
                    card_copies[index + 1 + i] += current_number_of_copies
        return card_copies


helpers.print_timed_results(day=2, solution_func=get_total_scratchcards)
