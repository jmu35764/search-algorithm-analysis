import unittest
from algorithms import (iterative_binary_search, recursive_binary_search, sequential_search)


class Test_Phase_1(unittest.TestCase):
    def test_iterative_binary_search(self):
        values = [3, 5, 8, 12, 14, 18, 21]
        values.sort()
        present_target = 12
        absent_target = 9
        index_present = iterative_binary_search(values, present_target)
        index_absent = iterative_binary_search(values, absent_target)
        self.assertEqual(index_present, 3)
        self.assertEqual(index_absent, -1)

    def test_ibs_first_element(self):
        values = [3, 5, 8, 12, 14, 18, 21]
        values.sort()
        present_target = 3
        index_present = iterative_binary_search(values, present_target)
        self.assertEqual(index_present, 0)

    def test_ibs_last_element(self):
        values = [3, 5, 8, 12, 14, 18, 21]
        values.sort()
        present_target = 21
        index_present = iterative_binary_search(values, present_target)
        self.assertEqual(index_present, 6)

    def test_ibs_one_element_present(self):
        values = [3]
        present_target = 3
        index_present = iterative_binary_search(values, present_target)
        self.assertEqual(index_present, 0)

    def test_ibs_one_element_absent(self):
        values = [3]
        absent_target = 9
        index_absent = iterative_binary_search(values, absent_target)
        self.assertEqual(index_absent, -1)

    def test_ibs_empty_list(self):
        values = []
        absent_target = 9
        index_absent = iterative_binary_search(values, absent_target)
        self.assertEqual(index_absent, -1)

    def test_ibs_duplicate_elements(self):
        values = [3, 5, 8, 8, 12, 14, 18, 21]
        values.sort()
        present_target = 8
        index_present = iterative_binary_search(values, present_target)
        self.assertEqual(index_present, 2)

    def test_recursive_binary_search(self):
        values = [3, 5, 8, 12, 14, 18, 21]
        values.sort()
        present_target = 12
        absent_target = 9
        index_present = recursive_binary_search(values, present_target, 0, len(values) - 1)
        index_absent = recursive_binary_search(values, absent_target, 0, len(values) - 1)
        self.assertEqual(index_present, 3)
        self.assertEqual(index_absent, -1)

    def test_rbs_first_element(self):
        values = [3, 5, 8, 12, 14, 18, 21]
        values.sort()
        present_target = 3
        index_present = recursive_binary_search(values, present_target, 0, len(values) - 1)
        self.assertEqual(index_present, 0)

    def test_rbs_last_element(self):
        values = [3, 5, 8, 12, 14, 18, 21]
        values.sort()
        present_target = 21
        index_present = recursive_binary_search(values, present_target, 0, len(values) - 1)
        self.assertEqual(index_present, 6)

    def test_rbs_one_element_present(self):
        values = [3]
        present_target = 3
        index_present = recursive_binary_search(values, present_target, 0, len(values) - 1)
        self.assertEqual(index_present, 0)

    def test_rbs_one_element_absent(self):
        values = [3]
        absent_target = 9
        index_absent = recursive_binary_search(values, absent_target, 0, len(values) - 1)
        self.assertEqual(index_absent, -1)

    def test_rbs_empty_list(self):
        values = []
        absent_target = 9
        index_absent = recursive_binary_search(values, absent_target, 0, len(values) - 1)
        self.assertEqual(index_absent, -1)

    def test_rbs_duplicate_elements(self):
        values = [3, 5, 8, 8, 12, 14, 18, 21]
        values.sort()
        present_target = 8
        index_present = recursive_binary_search(values, present_target, 0, len(values) - 1  )
        self.assertEqual(index_present, 2)

    def test_sequential_search(self):
        values = [3, 5, 8, 12, 14, 18, 21]
        values.sort()
        present_target = 12
        absent_target = 9
        index_present = sequential_search(values, present_target)
        index_absent = sequential_search(values, absent_target)
        self.assertEqual(index_present, 3)
        self.assertEqual(index_absent, -1)

    def test_seq_first_element(self):
        values = [3, 5, 8, 12, 14, 18, 21]
        values.sort()
        present_target = 3
        index_present = sequential_search(values, present_target)
        self.assertEqual(index_present, 0)

    def test_seq_last_element(self):
        values = [3, 5, 8, 12, 14, 18, 21]
        values.sort()
        present_target = 21
        index_present = sequential_search(values, present_target)
        self.assertEqual(index_present, 6)

    def test_seq_one_element_present(self):
        values = [3]
        present_target = 3
        index_present = sequential_search(values, present_target)
        self.assertEqual(index_present, 0)

    def test_seq_one_element_absent(self):
        values = [3]
        absent_target = 9
        index_absent = sequential_search(values, absent_target)
        self.assertEqual(index_absent, -1)

    def test_seq_empty_list(self):
        values = []
        absent_target = 9
        index_absent = sequential_search(values, absent_target)
        self.assertEqual(index_absent, -1)


if __name__ == '__main__':
    unittest.main()
