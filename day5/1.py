import bisect
import math
import os
import re
from dataclasses import dataclass
import helpers


@dataclass(frozen=True)
class MappingGuide:
    source: int
    destination: int
    span: int

    def __lt__(self, other):
        return self.source < other.source


def get_nearest_seed_location(file_path: os.path) -> int:
    seeds, mappings = _get_seeds_and_mappings(file=file_path)
    locations = []
    for seed in seeds:
        locations.append(_trace_through_mappings(seed=seed, mappings=mappings))
    return min(locations)


def _trace_through_mappings(seed: int, mappings: list[dict[str, list[int]]]) -> int:
    number_to_map = seed
    for mapping in mappings:
        index = bisect.bisect_right(mapping["sources"], number_to_map) - 1
        source = mapping["sources"][index]
        destination = mapping["destinations"][index]
        mapped_value = number_to_map + destination - source
        number_to_map = mapped_value
    return number_to_map


def _get_seeds_and_mappings(
    file: os.path,
) -> tuple[list[int], list[dict[str, list[int]]]]:
    with open(file) as puzzle_input:
        blocks = puzzle_input.read().split("\n\n")
        seeds = list(map(int, re.findall(r"\d+", blocks[0])))
        mappings = []
        for block in blocks[1:]:
            mapping = dict()
            guides = block.split(":")[1].strip().splitlines()
            sources = [-1]
            destinations = [-1]
            mapping_guides = []
            for guide in guides:
                destination = int(guide.split()[0])
                source = int(guide.split()[1])
                span = int(guide.split()[2])
                mapping_guides.append(
                    MappingGuide(source=source, destination=destination, span=span)
                )
            end_of_mapping = []
            for mapping_guide in sorted(mapping_guides):
                sources.append(mapping_guide.source)
                destinations.append(mapping_guide.destination)
                end_of_mapping.append(mapping_guide.source + mapping_guide.span)
            end_of_guides = max(end_of_mapping)
            sources.append(end_of_guides)
            destinations.append(end_of_guides)
            sources.append(math.inf)
            destinations.append(math.inf)
            mapping["sources"] = sources
            mapping["destinations"] = destinations
            mappings.append(mapping)
        return seeds, mappings


helpers.print_timed_results(solution_func=get_nearest_seed_location)
