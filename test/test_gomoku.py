import unittest
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

    def test_that_board_is_empty_at_start(self):
        for col in range(7):
            for row in range(6):
                self.assertTrue(self.gamemodel.is_valid_move(row, col))
                self.assertEqual(' ', self.gamemodel.get_piece(row, col))

    def test_that_game_has_no_winner_at_start(self):
        result = self.gamemodel.get_winner()
        self.assertEqual(' ', result)

    def test_that_red_player_is_next(self):
        self.evManager.Post(MouseInputEvent((1, 1)))
        result = self.gamemodel.get_next_player()
        self.assertEqual('red', result)

    def test_that_five_horizontal_in_row_wins(self):
        winner_row = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
        for i in range(5):
            self.evManager.Post(MouseInputEvent(winner_row[i]))
            self.evManager.Post(MouseInputEvent((1, i)))

        result = self.gamemodel.get_winner()
        self.assertEqual('black', result)

    def test_that_five_vertical_in_row_wins(self):
        winner_row = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
        for i in range(5):
            self.evManager.Post(MouseInputEvent(winner_row[i]))
            self.evManager.Post(MouseInputEvent((0, i + 1)))

        result = self.gamemodel.get_winner()
        self.assertEqual('black', result)

    def test_that_five_diagonal_left_in_row_wins(self):
        winner_row = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
        for i in range(5):
            self.evManager.Post(MouseInputEvent(winner_row[i]))
            self.evManager.Post(MouseInputEvent((0, i + 1)))

        result = self.gamemodel.get_winner()
        self.assertEqual('black', result)

    def test_that_five_diagonal_right_in_row_wins(self):
        winner_row = [(0, 6), (1, 5), (2, 4), (3, 3), (4, 2)]
        for i in range(5):
            self.evManager.Post(MouseInputEvent(winner_row[i]))
            self.evManager.Post(MouseInputEvent((0, i)))

        result = self.gamemodel.get_winner()
        self.assertEqual('black', result)

    def test_clicking_outside_grid_does_not_crash_game(self):
        click_positions = ((1, 1), (2, 3), (9, 7))
        for pos in click_positions:
            self.evManager.Post(MouseInputEvent(pos))
        result = self.gamemodel.get_winner()
        self.assertEqual(' ', result)


if __name__ == '__main__':
    unittest.main()
