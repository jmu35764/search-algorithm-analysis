import unittest
import random
import time
from algorithms import (iterative_binary_search, recursive_binary_search, sequential_search)

def main():

    data_sizes = [5_000, 50_000, 100_000, 150_000, 1_000_000]
    number_of_trials = 10
    ibs_times = []
    rbs_times = []
    ss_times = []

    for size in data_sizes:
        for _ in range(number_of_trials):  
            values = sorted(random.randint(1, 1_000_000) for _ in range(size))
            if random.random() < 0.5:
                target = random.choice(values)
            else:
                target = 1_000_001  # Ensure the target is not present in the list

            start = time.perf_counter()
            index = iterative_binary_search(values, target)
            elapsed_microseconds = (time.perf_counter() - start) * 1_000_000
            ibs_times.append(elapsed_microseconds)

            #print(f"Iterative Binary Search: Size {size}, Target {target}, Index {index}, Time {elapsed_microseconds:.2f} microseconds")

            start = time.perf_counter()
            index = recursive_binary_search(values, target, 0, len(values) - 1)
            elapsed_microseconds = (time.perf_counter() - start) * 1_000_000
            rbs_times.append(elapsed_microseconds)

            #print(f"Recursive Binary Search: Size {size}, Target {target}, Index {index}, Time {elapsed_microseconds:.2f} microseconds")

            start = time.perf_counter()
            index = sequential_search(values, target)
            elapsed_microseconds = (time.perf_counter() - start) * 1_000_000
            ss_times.append(elapsed_microseconds)

            #print(f"Sequential Search: Size {size}, Target {target}, Index {index}, Time {elapsed_microseconds:.2f} microseconds \n")

        print(f"Iterative Binary Search Times (microseconds): {ibs_times}")
        print(f"Recursive Binary Search Times (microseconds): {rbs_times}")
        print(f"Sequential Search Times (microseconds): {ss_times}")

        ibs_times.clear()
        rbs_times.clear()
        ss_times.clear()

if __name__ == "__main__":
    main()
