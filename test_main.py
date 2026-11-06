import unittest
from main import insertion_sort, merge_sort

class SortingTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(insertion_sort([]), ([], 0, 0))
    def test_small(self):
        self.assertEqual(insertion_sort([4, 1, 3, 2])[0], [1, 2, 3, 4])
    def test_sorted(self):
        sorted_values, comps, shifts = insertion_sort([1, 2, 3, 4])
        self.assertEqual(sorted_values, [1, 2, 3, 4])
        self.assertEqual(comps, 3)
        self.assertEqual(shifts, 0)
    def test_merge(self):
        self.assertEqual(merge_sort([4, 1, 3, 2]), [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
