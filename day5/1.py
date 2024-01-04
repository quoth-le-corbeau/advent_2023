import bisect
import math
import os
from dataclasses import dataclass
import helpers


@dataclass(frozen=True)
class MappingGuide:
    destination: int
    source: int
    span: int

    def __lt__(self, other):
        return self.source < other.source


def find_min_seed_location(file_path: os.path) -> int:
    seeds, mappings = _get_seeds_and_mappings(file=file_path)
    mapped_seeds = []
    for seed in seeds:
        mapped_seeds.append(_trace_through_mappings(seed=seed, mappings=mappings))
    return min(mapped_seeds)


def _trace_through_mappings(seed: int, mappings: list[dict[str, list[float]]]) -> int:
    mapped_seed = seed
    for mapping in mappings:
        index = bisect.bisect_right(mapping["sources"], mapped_seed) - 1
        source = mapping["sources"][index]
        destination = mapping["destinations"][index]
        mapped_seed = destination + mapped_seed - source
    return mapped_seed


def _get_seeds_and_mappings(file: os.path):
    with open(file) as puzzle_input:
        seeds, *blocks = puzzle_input.read().split("\n\n")
        seeds = list(map(int, seeds.split(":")[1].strip().split()))
        mappings = list()
        for block in blocks:
            mapping = _get_full_mapping(block=block)
            mappings.append(mapping)
    return seeds, mappings


def _get_full_mapping(block: str) -> dict[str, list[int]]:
    guides = block.split(":")[1].strip().splitlines()
    mapping = dict()
    sources = [-1]
    destinations = [-1]
    mapping_guides = []
    for guide in guides:
        destination, source, span = [int(val) for val in guide.split()]
        mapping_guides.append(
            MappingGuide(destination=destination, source=source, span=span)
        )
    mapping = _make_full_mapping(destinations, mapping, mapping_guides, sources)
    return mapping


def _make_full_mapping(
    destinations: list[int],
    mapping: dict[str, list[int]],
    mapping_guides: list[MappingGuide],
    sources: list[int],
) -> dict[str, list[int]]:
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
    return mapping


helpers.print_timed_results(solution_func=find_min_seed_location)
