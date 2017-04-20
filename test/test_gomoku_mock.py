import unittest
from mock import MagicMock
from app.eventmanager import EventManager
from app.eventmanager import QuitEvent
from app.eventmanager import MouseInputEvent
from app.model import GameEngine

class TddInPythonExample(unittest.TestCase):

    def setUp(self):
        self.evManager = EventManager()
        self.gamemodel = GameEngine(self.evManager, 7, 6)

    def tearDown(self):
        self.evManager.Post(QuitEvent())

    def test_that_black_player_starts(self):
        result = self.gamemodel.get_next_player()
        self.assertEqual('black', result)

    def test_that_game_has_no_winner_at_start(self):
        result = self.gamemodel.get_winner()
        self.assertEqual(' ', result)

    def test_that_red_player_is_next(self):
        self.evManager.Post(MouseInputEvent((1, 1)))
        result = self.gamemodel.get_next_player()
        self.assertEqual('red', result)

    def test_that_five_vertical_in_row_wins(self):
        winner_row = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
        for i in range(5):
            self.evManager.Post(MouseInputEvent(winner_row[i]))
            self.evManager.Post(MouseInputEvent((1, i)))

        result = self.gamemodel.get_winner()
        self.assertEqual('black', result)

    def test_that_five_horizontal_in_row_wins(self):
        winner_row = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
        for i in range(5):
            self.evManager.Post(MouseInputEvent(winner_row[i]))
            self.evManager.Post(MouseInputEvent((0, i)))

        result = self.gamemodel.get_winner()
        self.assertEqual('black', result)



if __name__ == '__main__':
    unittest.main()
