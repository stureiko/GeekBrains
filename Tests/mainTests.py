import unittest
import src.avasales as aviasales


class aviasalesTest(unittest.TestCase):
    def test_blank(self):
        self.assertEqual(aviasales.iata_search(''), [])
    #
    # def test_city(self):
    #     self.assertEqual(aviasales.iata_search('Москва'), ['Russia', 'Moscow', 'MOW'])


if __name__ == '__main__':
    unittest.main()
