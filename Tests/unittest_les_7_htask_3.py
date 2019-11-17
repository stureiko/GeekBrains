import unittest
import random
import statistics
from src.les_7_htask_3 import quick_median, pivot_func


class MedianTest(unittest.TestCase):
    def test_median(self):
        size = random.randint(0, 100)
        width = size * 10
        array = [random.randint(0, width) for _ in range(2 * size + 1)]
        self.assertEqual(statistics.median(array), quick_median(array, pivot_func))


if __name__ == '__main__':
    unittest.main()
