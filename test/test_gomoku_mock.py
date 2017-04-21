import unittest
from mock import patch
from app.eventmanager import EventManager
from app.eventmanager import QuitEvent
from app.eventmanager import MouseInputEvent
from app.view import GraphicalView
from app.model import GameEngine
from app import *

class TddInPythonExample(unittest.TestCase):

    @patch.object(GraphicalView, 'initialize')
    # This is the same thing
    # @patch('pyqueue.queue.Queue._get_queue')
    def test_queue_initialization(self, initialize_view_mock):
        """
        Can use either path or patch.object as Queue object is
        imported.

         * To check that a method called only once:
           `assert_called_once_with`
         * To check the last call: `assert_called_with`
         * To check that a particular call is done among other:
           `assert_any_call`

        """
        evManager = EventManager()
        gamemodel = GameEngine(evManager, 7, 6)
        view = GraphicalView(evManager, gamemodel, 7, 6)
        initialize_view_mock.assert_any_call()

if __name__ == '__main__':
    unittest.main()
