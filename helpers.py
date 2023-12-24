import os
import time


def print_timed_results(
    day: int, solution_func: callable, test_path_extension: str = "eg.txt"
):
    path_route = os.path.basename("day" + str(day) + "/")
    test_path = path_route + test_path_extension
    real_path = path_route + "input.txt"

    start = time.perf_counter()
    print(solution_func(test_path))
    print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
    start = time.perf_counter()
    print(solution_func(real_path))
    print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
