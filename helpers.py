import time


def print_timed_results(solution_func: callable, test_path_extension: str = "eg.txt"):
    test_path = test_path_extension
    real_path = "input.txt"

    start = time.perf_counter()
    print(solution_func(test_path))
    print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
    start = time.perf_counter()
    print(solution_func(real_path))
    print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
