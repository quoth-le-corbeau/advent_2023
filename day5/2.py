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
    seed_ranges, mappings = _get_seeds_and_mappings(file=file_path)
    location_ranges = []
    location_ranges += _trace_range_through_mappings(
        seed_ranges=seed_ranges, mappings=mappings
    )
    return min([location[0] for location in location_ranges])


def _trace_range_through_mappings(
    seed_ranges: list[tuple[int, int]], mappings: list[list[int]]
) -> list[tuple[int, int]]:
    result = []
    while len(seed_ranges) > 0:
        start, end = seed_ranges.pop()
    for destination, source, span in mappings:
        overlap_start = max(start, source)
        overlap_end = min(end, source + span)
        if overlap_start < overlap_end:
            result.append(
                (
                    overlap_start - source + destination,
                    overlap_end - source + destination,
                )
            )
            # may not have perfect match
            if overlap_start > start:
                seed_ranges.append((start, overlap_start))
            if end > overlap_end:
                seed_ranges.append((overlap_end, end))
            break
        else:
            result.append((start, end))
    return result


def _get_seeds_and_mappings(
    file: os.path,
) -> tuple[list[tuple[int, int]], list[list[int]]]:
    with open(file) as puzzle_input:
        blocks = puzzle_input.read().split("\n\n")
        seeds_and_ranges = list(map(int, blocks[0].split(":")[1].split()))
        seed_ranges = []
        for i in range(0, len(seeds_and_ranges), 2):
            seed_ranges.append(
                (seeds_and_ranges[i], seeds_and_ranges[i] + seeds_and_ranges[i + 1])
            )
        mappings = []
        for block in blocks[1:]:
            for line in block.splitlines()[1:]:
                mappings.append(list(map(int, line.split())))
        return seed_ranges, mappings


helpers.print_timed_results(solution_func=get_nearest_seed_location)
