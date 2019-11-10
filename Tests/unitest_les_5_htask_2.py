import unittest
from src.les_5_htask_2 import plus

class PlusTest(unittest.TestCase):
    def test_0(self):
        s1 = '1D'
        s2 = '2A'
        self.assertEqual(plus(s2, s1), hex((int(s1, 16) + int(s2, 16))), '0 + 1A = 1A')


if __name__ == '__main__':
    unittest.main()
