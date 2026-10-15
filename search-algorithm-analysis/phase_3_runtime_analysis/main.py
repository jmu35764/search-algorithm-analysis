import unittest
import random
import time
from algorithms import (iterative_binary_search, recursive_binary_search, sequential_search)

def main():

    data_sizes = [5_000, 50_000, 100_000, 150_000, 1_000_000]
    number_of_trials = 10

    for size in data_sizes:
          
        values = sorted(random.randint(1, size) for _ in range(size))
        if random.random() < 0.5:
            target = random.choice(values)
        else:
            target = 5_001  # Ensure the target is not present in the list

        start = time.perf_counter()
        index = iterative_binary_search(values, target)
        elapsed_microseconds = (time.perf_counter() - start) * 1_000_000

        print(f"Iterative Binary Search: Size {size}, Target {target}, Index {index}, Time {elapsed_microseconds:.2f} microseconds")

        start = time.perf_counter()
        index = recursive_binary_search(values, target, 0, len(values) - 1)
        elapsed_microseconds = (time.perf_counter() - start) * 1_000_000

        print(f"Recursive Binary Search: Size {size}, Target {target}, Index {index}, Time {elapsed_microseconds:.2f} microseconds")

        start = time.perf_counter()
        index = sequential_search(values, target)
        elapsed_microseconds = (time.perf_counter() - start) * 1_000_000

        print(f"Sequential Search: Size {size}, Target {target}, Index {index}, Time {elapsed_microseconds:.2f} microseconds \n")

if __name__ == "__main__":
    main()
