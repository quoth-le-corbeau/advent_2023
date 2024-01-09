import math
import os
import helpers


def count_ghost_moves_to_navigate_wasteland(file_path: os.path) -> int:
    directional_instructions, network_look_up = _parse_instructions(file=file_path)
    number_of_directional_instructions = len(directional_instructions)
    start_positions = [key for key in network_look_up if key.endswith("A")]
    distances_to_zs = []
    for string in start_positions:
        i = 0
        distances_to_z = []
        while not string.endswith("Z"):
            if i >= number_of_directional_instructions:
                direction = directional_instructions[
                    i % number_of_directional_instructions
                ]
            else:
                direction = directional_instructions[i]
            string = network_look_up[string][int(direction)]
            i += 1
        distances_to_z.append(i)
        distances_to_zs += distances_to_z
    lcm = 1
    for number in distances_to_zs:
        lcm = lcm * number // math.gcd(lcm, number)
    return lcm


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
    solution_func=count_ghost_moves_to_navigate_wasteland, test_path_extension="eg2.txt"
)
