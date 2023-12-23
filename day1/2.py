import re
from pathlib import Path

import helpers

SPELLED_DIGITS = "one two three four five six seven eight nine".split()


def sum_calibration_values(file_path: Path) -> int:
    return find_and_sum_spelled_digits(file=file_path)


def find_and_sum_spelled_digits(file: Path) -> int:
    with open(file) as puzzle_input:
        lines = puzzle_input.readlines()
        pattern = "(?=(one|two|three|four|five|six|seven|eight|nine|\\d))"
        # pattern = "(?=(" + "|".join(SPELLED_DIGITS) + "|\\d))"  # equivalent
        all_calibration_values = []
        for line in lines:
            line = line.strip()
            all_digits = list(map(_convert_digit, re.findall(pattern, line)))
            all_calibration_values.append((all_digits[0] * 10) + all_digits[-1])
        return sum(all_calibration_values)


def _convert_digit(string: str) -> int:
    if string.isdigit():
        return int(string)
    else:
        return SPELLED_DIGITS.index(string) + 1


helpers.print_timed_results(day=2, solution_func=sum_calibration_values)
