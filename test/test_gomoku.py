import unittest
from app.eventmanager import EventManager
from app.model import GameEngine

class TddInPythonExample(unittest.TestCase):

    def setUp(self):
        self.evManager = EventManager()
        self.gamemodel = GameEngine(self.evManager, 7, 6)
        self.gamemodel.run()

    def test_that_black_player_starts(self):
        result = self.gamemodel.get_next_player()
        self.assertEqual('black', result)



if __name__ == '__main__':
    unittest.main()
