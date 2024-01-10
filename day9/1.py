import dataclasses
import os
import re
import itertools
from dataclasses import dataclass
import helpers


@dataclass(frozen=True)
class SeriesWithAllDifference:
    series: list[int]
    all_difference: list[list[int]]


def sum_next_terms_in_series(file_path: os.path) -> int:
    all_series = _get_all_series_from_input(file=file_path)
    print(f"{all_series=}")
    series_with_ordered_differences = _get_ordered_difference_series(
        all_series=all_series
    )
    next_terms_in_series = _get_all_next_terms_in_series(
        series_with_ordered_differences=series_with_ordered_differences
    )
    return sum(next_terms_in_series)


def _get_all_next_terms_in_series(
    series_with_ordered_differences: list[SeriesWithAllDifference],
) -> list[int]:
    """Problem seems to be here"""
    next_terms_in_series = list()
    for series_with_ordered_differences in series_with_ordered_differences:
        step_to_next_term = 0
        for difference_series in series_with_ordered_differences.all_difference:
            difference_series.append(difference_series[-1] + step_to_next_term)
            step_to_next_term = difference_series[-1]
        next_term_in_series = (
            series_with_ordered_differences.series[-1] + step_to_next_term
        )
        # series.series.append(next_term_in_series)
        next_terms_in_series.append(next_term_in_series)
    return next_terms_in_series


def _get_ordered_difference_series(
    all_series: list[list[int]],
) -> list[SeriesWithAllDifference]:
    all_series_with_all_differences = list()
    for series in all_series:
        all_series_with_all_differences.append(
            _get_all_difference_series(series=series)
        )
    all_series_with_all_differences_ordered = list()
    for all_series in all_series_with_all_differences:
        all_series = dataclasses.replace(
            all_series, all_difference=all_series.all_difference[::-1]
        )
        all_series_with_all_differences_ordered.append(all_series)
    return all_series_with_all_differences_ordered


def _get_all_difference_series(series: list[int]) -> SeriesWithAllDifference:
    current_series = series
    series_with_all_difference = SeriesWithAllDifference(
        series=series, all_difference=list()
    )
    while not all(
        difference == 0 for difference in _get_common_difference(current_series)
    ):
        current_series = _get_common_difference(current_series)
        series_with_all_difference.all_difference.append(current_series)
    return series_with_all_difference


def _get_common_difference(integers: list[int]) -> list[int]:
    return [y - x for x, y in itertools.pairwise(integers)]


def _get_all_series_from_input(file: os.path) -> list[list[int]]:
    with open(file) as puzzle_input:
        lines = puzzle_input.read().strip().splitlines()
        all_series = list()
        for line in lines:
            series = list(map(int, re.findall(r"\d+|-\d+", line)))
            all_series.append(series)
        return all_series


helpers.print_timed_results(solution_func=sum_next_terms_in_series)
