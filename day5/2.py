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
    seed_ranges, mappings = _get_seed_ranges_and_mappings(file=file_path)
    mapped_seed_ranges = []
    for seed_range in seed_ranges:
        mapped_seed_ranges += _trace_range_through_mappings(
            seed_range=seed_range, mappings=mappings
        )
    print(f"{mapped_seed_ranges=}")
    return min([mapped_seed_range[0] for mapped_seed_range in mapped_seed_ranges])


def _trace_range_through_mappings(
    seed_range: tuple[int, int], mappings: list[dict[str, list[float]]]
) -> list[tuple[int, int]]:
    result = list()
    start, end = seed_range
    for mapping in mappings:
        start_index = bisect.bisect_right(mapping["sources"], start) - 1
        end_index = bisect.bisect_right(mapping["sources"], end)
        start_source = mapping["sources"][start_index]
        start_destination = mapping["destinations"][start_index]
        end_source = mapping["sources"][end_index]
        end_destination = mapping["destinations"][end_index]
        result.append(
            (
                start_destination + start - start_source,
                end_destination + end - end_source,
            )
        )
    return result


def _get_seed_ranges_and_mappings(file: os.path):
    with open(file) as puzzle_input:
        seeds, *blocks = puzzle_input.read().split("\n\n")
        seeds = list(map(int, seeds.split(":")[1].strip().split()))
        seed_ranges = [
            (seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)
        ]
        mappings = list()
        for block in blocks:
            mapping = _get_full_mapping(block=block)
            mappings.append(mapping)
    return seed_ranges, mappings


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
