import unittest

from app.events import EventManager
from app.events import MouseInputEvent
from app.events import QuitEvent
from app.model import GameEngine
from app.model import PLAYER_RED, PLAYER_BLACK, UNKNOWN

HEIGHT = 6
WIDTH = 7


class TestGame(unittest.TestCase):
    """solutions/iteration_2
    Remaining from spec:
    2. The color of next player should always be shown
    5. When a player clicks on a position, a marker should be shown there
    6. When a player has won, the players color should show as winner
    """

    def setUp(self):
        self.evManager = EventManager()
        self.game = GameEngine(self.evManager, HEIGHT, WIDTH)

    def tearDown(self):
        self.evManager.Post(QuitEvent())

    def test_that_board_is_empty_at_start(self):
        """1. An empty board should be shown when new games starts"""
        for col in range(WIDTH):
            for row in range(HEIGHT):
                self.assertTrue(self.game.is_valid_move(row, col))
                self.assertEqual(UNKNOWN, self.game.get_piece(row, col))

    def test_that_black_player_starts(self):
        """3. Black player always starts"""
        self.assertEqual(PLAYER_BLACK, self.game.get_next_player())

    def test_that_game_has_no_winner_at_start(self):
        self.assertEqual(UNKNOWN, self.game.get_winner())

    def test_that_red_player_is_next(self):
        """4a. When a player has placed a marker it is the other players turn"""
        self.evManager.Post(MouseInputEvent((1, 1)))
        self.assertEqual(PLAYER_RED, self.game.get_next_player())

    def test_that_five_horizontal_in_row_wins(self):
        """7a. When a player has 5 in a row, the player has won"""
        winner_row = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
        for i in range(5):
            self.evManager.Post(MouseInputEvent(winner_row[i]))
            self.evManager.Post(MouseInputEvent((1, i)))
        self.assertEqual(PLAYER_BLACK, self.game.get_winner())

    def test_that_five_vertical_in_row_wins(self):
        """7b. When a player has 5 in a row, the player has won"""
        winner_row = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
        self.assertEqual(UNKNOWN, self.game.get_winner())
        for i in range(5):
            self.evManager.Post(MouseInputEvent(winner_row[i]))
            self.evManager.Post(MouseInputEvent((0, i + 1)))
        self.assertEqual(PLAYER_BLACK, self.game.get_winner())

    def test_that_five_diagonal_left_in_row_wins(self):
        """7c. When a player has 5 in a row, the player has won"""
        winner_row = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
        for i in range(5):
            self.evManager.Post(MouseInputEvent(winner_row[i]))
            self.evManager.Post(MouseInputEvent((0, i + 1)))
        self.assertEqual(PLAYER_BLACK, self.game.get_winner())

    def test_that_five_diagonal_right_in_row_wins(self):
        """7d. When a player has 5 in a row, the player has won"""
        winner_row = [(0, 6), (1, 5), (2, 4), (3, 3), (4, 2)]
        for i in range(5):
            self.evManager.Post(MouseInputEvent(winner_row[i]))
            self.evManager.Post(MouseInputEvent((0, i)))
        self.assertEqual(PLAYER_BLACK, self.game.get_winner())

    def test_clicking_outside_grid_does_not_crash_game(self):
        click_positions = ((1, 1), (2, 3), (HEIGHT + 3, WIDTH))
        for pos in click_positions:
            self.evManager.Post(MouseInputEvent(pos))
        self.assertEqual(UNKNOWN, self.game.get_winner())


if __name__ == '__main__':
    unittest.main()
