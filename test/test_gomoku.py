import unittest

from app.model import PLAYER_RED, PLAYER_BLACK, UNKNOWN
from app.events import EventManager
from app.events import QuitEvent
from app.events import MouseInputEvent
from app.model import GameEngine

RED = PLAYER_RED
BLACK = PLAYER_BLACK


class TddInPythonExample(unittest.TestCase):
    def setUp(self):
        self.evManager = EventManager()
        self.game = GameEngine(self.evManager, 7, 6)

    def tearDown(self):
        self.evManager.Post(QuitEvent())

    def test_that_game_has_no_winner_at_start(self):
        self.assertEqual(UNKNOWN, self.game.get_winner())

    def test_that_five_horizontal_in_row_wins(self):
        winner_row = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
        for i in range(5):
            self.evManager.Post(MouseInputEvent(winner_row[i]))
            self.evManager.Post(MouseInputEvent((1, i)))
        self.assertEqual(BLACK, self.game.get_winner())


if __name__ == '__main__':
    unittest.main()
