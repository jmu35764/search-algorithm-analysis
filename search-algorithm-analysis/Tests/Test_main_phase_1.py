from algorithms import (iterative_binary_search, recursive_binary_search, sequential_search)
import unittest

class Test_Phase_1(unittest.TesetCase):
    def test_iterative_binary_search(self):
        values = [3, 5, 8, 12, 14, 18, 21]
        values.sort()
        present_target = 12
        absent_target = 9
        index_present = iterative_binary_search(values, present_target)
        index_absent = iterative_binary_search(values, absent_target)
        self.assertEqual(index_present, 3)
        self.assertEqual(index_absent, -1)


if __name__ == '__main__':
    unittest.main()