import re
from pathlib import Path

from helpers import print_timed_results


def sum_calibration_values(file_path: Path) -> int:
    values = _parse_file(file=file_path)
    return sum(values)


def _parse_file(file: Path) -> list[int]:
    with open(file) as puzzle_input:
        lines = puzzle_input.readlines()
        all_digits = []
        for line in lines:
            print(line)
            digits = re.findall(r"\d+", line)
            print(digits)


print_timed_results(day=1, solution_func=sum_calibration_values)
