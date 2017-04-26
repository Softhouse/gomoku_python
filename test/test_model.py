import unittest

from app.model import PLAYER_RED, PLAYER_BLACK, UNKNOWN
from app.events import EventManager
from app.events import QuitEvent
from app.model import GameEngine


class TestGame(unittest.TestCase):
    """
    (solutions/beginning)
    There should only be one failing test to show
    structure of test
    """
    def setUp(self):
        self.evManager = EventManager()
        self.game = GameEngine(self.evManager, 7, 6)

    def tearDown(self):
        self.evManager.Post(QuitEvent())

    def test_that_game_has_no_winner_at_start(self):
        self.assertEqual(UNKNOWN, self.game.get_winner())


if __name__ == '__main__':
    unittest.main()
