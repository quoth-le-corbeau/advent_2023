import os
import helpers


def count_moves_to_navigate_wasteland(file_path: os.path) -> int:
    directional_instructions, network_look_up = _parse_instructions(file=file_path)
    number_of_directional_instructions = len(directional_instructions)
    current_strings = list()
    for key, _ in network_look_up.items():
        if key.endswith("A"):
            current_strings.append(key)
    i = 0
    while not all([current_string.endswith("Z") for current_string in current_strings]):
        if i >= number_of_directional_instructions:
            direction = directional_instructions[i % number_of_directional_instructions]
        else:
            direction = directional_instructions[i]
        direction = int(direction)
        current_strings = [
            network_look_up[current_string][direction]
            for current_string in current_strings
        ]
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
