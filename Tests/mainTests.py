import unittest
from src.player import Player
from src.game import Game


class PlayerTest(unittest.TestCase):
    def test_default_health(self):
        p = Player()
        self.assertEqual(100, p.health, 'Здоровье игрока по умолчанию должно быть равно 100')

    def test_default_damage(self):
        p = Player()
        self.assertEqual(10, p.default_damage, 'Удар игрока по умолчанию должен быть равен 10')

    def test_default_position(self):
        p = Player()
        self.assertListEqual([0, 0], p.position, 'Координаты игрока по умолчанию равны [0, 0]')


class GameTest(unittest.TestCase):
    def test_default_game_player_health(self):
        game = Game()
        self.assertEqual(100, game.player.health, 'Здоровье игрока созданного по умолчанию должно быть равно 100')

    def test_default_game_player_damage(self):
        game = Game()
        self.assertEqual(10, game.player.default_damage, 'Удар игрока созданного по умолчанию должен быть равен 10')


if __name__ == '__main__':
    unittest.main()
