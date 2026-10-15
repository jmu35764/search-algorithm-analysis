import unittest
import random
from algorithms import (iterative_binary_search, recursive_binary_search, sequential_search)


class Test_Phase_2(unittest.TestCase):
    def setUp(self):
        # Generate a large sorted list of random integers for testing
        values = [random.randint(1, 100) for _ in range(20)]
        values.sort()
        if random.random() < 0.5:
            target = random.choice(values)
            expected_to_be_present = True
        else:
            target = 101
            expected_to_be_present = False

    def test_iterative_binary_search_large_list(self):
        

    
