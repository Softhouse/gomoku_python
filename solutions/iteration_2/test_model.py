import unittest

from app.model import PLAYER_RED, PLAYER_BLACK, UNKNOWN
from app.events import EventManager
from app.events import QuitEvent
from app.events import MouseInputEvent
from app.model import GameEngine


class TestGame(unittest.TestCase):
    """solutions/iteration_2"""
    def setUp(self):
        self.evManager = EventManager()
        self.game = GameEngine(self.evManager, 7, 6)

    def tearDown(self):
        self.evManager.Post(QuitEvent())

    def test_that_black_player_starts(self):
        self.assertEqual(PLAYER_BLACK, self.game.get_next_player())

    def test_that_board_is_empty_at_start(self):
        for col in range(7):
            for row in range(6):
                self.assertTrue(self.game.is_valid_move(row, col))
                self.assertEqual(UNKNOWN, self.game.get_piece(row, col))

    def test_that_game_has_no_winner_at_start(self):
        self.assertEqual(UNKNOWN, self.game.get_winner())

    def test_that_red_player_is_next(self):
        self.evManager.Post(MouseInputEvent((1, 1)))
        self.assertEqual(PLAYER_RED, self.game.get_next_player())

    def test_that_five_horizontal_in_row_wins(self):
        winner_row = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
        for i in range(5):
            self.evManager.Post(MouseInputEvent(winner_row[i]))
            self.evManager.Post(MouseInputEvent((1, i)))
        self.assertEqual(PLAYER_BLACK, self.game.get_winner())

    def test_that_five_vertical_in_row_wins(self):
        winner_row = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
        self.assertEqual(UNKNOWN, self.game.get_winner())
        for i in range(5):
            self.evManager.Post(MouseInputEvent(winner_row[i]))
            self.evManager.Post(MouseInputEvent((0, i + 1)))
        self.assertEqual(PLAYER_BLACK, self.game.get_winner())

    def test_that_five_diagonal_left_in_row_wins(self):
        winner_row = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
        for i in range(5):
            self.evManager.Post(MouseInputEvent(winner_row[i]))
            self.evManager.Post(MouseInputEvent((0, i + 1)))
        self.assertEqual(PLAYER_BLACK, self.game.get_winner())

    def test_that_five_diagonal_right_in_row_wins(self):
        winner_row = [(0, 6), (1, 5), (2, 4), (3, 3), (4, 2)]
        for i in range(5):
            self.evManager.Post(MouseInputEvent(winner_row[i]))
            self.evManager.Post(MouseInputEvent((0, i)))
        self.assertEqual(PLAYER_BLACK, self.game.get_winner())

    def test_clicking_outside_grid_does_not_crash_game(self):
        click_positions = ((1, 1), (2, 3), (9, 7))
        for pos in click_positions:
            self.evManager.Post(MouseInputEvent(pos))
        self.assertEqual(UNKNOWN, self.game.get_winner())


if __name__ == '__main__':
    unittest.main()
