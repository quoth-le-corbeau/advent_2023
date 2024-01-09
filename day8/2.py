import os
import re
import helpers


def count_moves_to_navigate_wasteland(file_path: os.path) -> int:
    directional_instructions, network_look_up = _parse_instructions(file=file_path)
    current_string_pattern = r"*\A$"
    final_string_pattern = r"*\Z$"
    number_of_directional_instructions = len(directional_instructions)
    i = 0
    while current_string != final_string:
        if i >= number_of_directional_instructions:
            direction = directional_instructions[i % number_of_directional_instructions]
        else:
            direction = directional_instructions[i]
        direction = int(direction)
        current_string = network_look_up[current_string][direction]
        i += 1
    return i


def _parse_instructions(file: os.path) -> tuple[str, dict[str, tuple[str, str]]]:
    with open(file) as puzzle_input:
        directional_instructions = puzzle_input.readline()
        network_look_up = dict()
        for line in puzzle_input.readlines()[1:]:
            line = line.strip().replace("(", "").replace(")", "")
            network_look_up[line.split(" = ")[0].strip()] = (
                line.split(" = ")[1].split(",")[0].strip(),
                line.split(" = ")[1].split(",")[1].strip(),
            )
        directional_instructions = directional_instructions.replace("L", "0").replace(
            "R", "1"
        )
    return directional_instructions.strip(), network_look_up


helpers.print_timed_results(
    solution_func=count_moves_to_navigate_wasteland, test_path_extension="eg2.txt"
)
