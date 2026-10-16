import unittest
import random
from algorithms import (iterative_binary_search, recursive_binary_search, sequential_search)

    
def main():

    # Generate a large sorted list of random integers for testing
    values = [random.randint(1, 100) for _ in range(20)]
    
    # Sort the values before running the algorithms
    values.sort()

    # Randomly decide whether to test with a present or absent target
    # Give the random value a name so it can be printed for debugging purposes
    random_num = random.random()

    if random_num < 0.5: # 50% chance to test with a present target
        target = random.choice(values)
        expected_to_be_present = True
    else:
        target = 101
        expected_to_be_present = False

    print(f"Testing with values: {values}")
    print(f"Random number: {random_num}")
    print(f"Target: {target}, Expected to be present:{expected_to_be_present}")

    iterative_index = iterative_binary_search(values, target)
    print(f"Iterative binary search index: {iterative_index}")

    recursive_index = recursive_binary_search(values, target, 0, len(values) - 1)
    print(f"Recursive binary search index: {recursive_index}")

    sequential_index = sequential_search(values, target)
    print(f"Sequential search index: {sequential_index}")

if __name__ == "__main__":
    main()