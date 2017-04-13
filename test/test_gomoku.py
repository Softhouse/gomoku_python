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

    def test_that_red_player_is_next(self):
        self.evManager.Post(MouseInputEvent((1, 1)))
        result = self.gamemodel.get_next_player()
        self.assertEqual('red', result)



if __name__ == '__main__':
    unittest.main()
