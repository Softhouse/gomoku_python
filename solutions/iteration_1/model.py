from events import *

CELL_EMPTY = 0
CELL_BLACK = 1
CELL_RED = 2

UNKNOWN = ' '
PLAYER_BLACK = 'black'
PLAYER_RED = 'red'


class GameEngine(object):
    """
    Tracks the game state.
    (solutions/iteration_1)
    """

    def __init__(self, evManager, cols, rows):
        self.cols = cols
        self.rows = rows
        self.grid = [[0 for x in range(cols)] for y in range(rows)]
        self.player = PLAYER_BLACK
        self.winner = UNKNOWN
        self.evManager = evManager
        evManager.RegisterListener(self)
        self.running = False

    def _switch_player(self):
        """Switch to other player"""
        self.player = PLAYER_RED if self.player == PLAYER_BLACK else PLAYER_BLACK

    def get_next_player(self):
        return self.player

    def _play_turn(self, pos):
        """Play one turn of the game. Takes care of house-keeping like
        1. Should game continue? (winner or exhaustion?)
        2. Can we move to 'pos'?
        3. Declare a winner?
        4. Switch to next player
        """
        row, col = pos
        if self.is_valid_move(row, col):
            self.grid[row][col] = CELL_BLACK if self.player == PLAYER_BLACK else CELL_RED
            self._switch_player()

    def is_valid_move(self, row, col):
        """
        Return True if it is valid to move to cell row, col. You cannot move to an occupied cell
        on grid or to a cell outside grid.
        """
        return self.grid[row][col] == CELL_EMPTY

    def get_piece(self, row, col):
        """
        Return piece in row, col of board. Enables View to find out what to draw on GUI
        """
        cell = self.grid[row][col]
        if cell == CELL_BLACK:
            return PLAYER_BLACK
        if cell == CELL_RED:
            return PLAYER_RED
        else:
            return UNKNOWN

    def get_winner(self):
        """Return winner of the game, enables View to declare winner and take appropriate action
        """
        return self.winner

    def is_winner(self, player):
        """Calculate if there is a winner or not. Check both colors and all combinations to determine this
        Return True iff there is a winner, else False
        """
        return False

    def notify(self, event):
        """
        Called by an event in the message queue.
        """

        if isinstance(event, QuitEvent):
            self.running = False
        elif isinstance(event, MouseInputEvent):
            self._play_turn(event.clickpos)

    def run(self):
        """
        Starts the game engine loop.
        This pumps a Tick event into the message queue for each loop.
        The loop ends when this object hears a QuitEvent in notify().
        """
        self.running = True
        self.evManager.Post(InitializeEvent())
        while self.running:
            newTick = TickEvent()
            self.evManager.Post(newTick)
