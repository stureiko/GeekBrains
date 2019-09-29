import unittest
import src.avasales as aviasales


class aviasalesTest(unittest.TestCase):
    def test_blank(self):
        self.assertEqual(aviasales.iata_search(''), [])


if __name__ == '__main__':
    unittest.main()
