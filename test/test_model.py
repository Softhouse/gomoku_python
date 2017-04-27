import unittest

from app.model import UNKNOWN
from app.events import EventManager
from app.events import QuitEvent
from app.model import GameEngine

ROW_COUNT = 6
COL_COUNT = 7


class TestGame(unittest.TestCase):
    """solutions/iteration_1
    There should be one working test here when the iteration is finished
    """
    def setUp(self):
        self.evManager = EventManager()
        self.game = GameEngine(self.evManager, COL_COUNT, ROW_COUNT)

    def tearDown(self):
        self.evManager.Post(QuitEvent())

    def test_that_board_is_empty_at_start(self):
        for col in range(COL_COUNT):
            for row in range(ROW_COUNT):
                self.assertTrue(self.game.is_valid_move(row, col))
                self.assertEqual(UNKNOWN, self.game.get_piece(row, col))

if __name__ == '__main__':
    unittest.main()
