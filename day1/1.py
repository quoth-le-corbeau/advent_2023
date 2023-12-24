import re
from pathlib import Path

import helpers


def sum_calibration_values(file_path: Path) -> int:
    return find_and_sum_digits(file=file_path)


def find_and_sum_digits(file: Path) -> int:
    with open(file) as puzzle_input:
        lines = puzzle_input.readlines()
        all_calibration_values = []
        for line in lines:
            all_digits = re.findall(r"[0-9]", line)
            calibration_value = f"{all_digits[0]}{all_digits[-1]}"
            all_calibration_values.append(int(calibration_value))
        return sum(all_calibration_values)


helpers.print_timed_results(
    day=1, solution_func=sum_calibration_values, test_path_extension="eg1.txt"
)
