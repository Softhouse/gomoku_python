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
    (solutions/beginning)
    """

    def __init__(self, evManager, cols, rows):
        """
        evManager (EventManager): Allows posting messages to the event queue.

        Attributes:
        running (bool): True while the engine is online. Changed via QuitEvent().
        """
        # Create a cols by row grid
        # 0 = ' ', 1 = black, 2 = red
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
        """Play one turn of the game"""
        row, col = pos
        if self.winner == UNKNOWN and self.is_valid_move(row, col):
            self.grid[row][col] = CELL_BLACK if self.player == PLAYER_BLACK else CELL_RED
            if self.is_winner(self.player):
                self.winner = self.player
            else:
                self._switch_player()

    def is_valid_move(self, row, col):
        """
        Return True if it is valid to move to position row, col
        """
        try:
            result = self.grid[row][col] == CELL_EMPTY
        except IndexError:
            result = False
        return result

    def get_piece(self, row, col):
        """
        Return piece in row, col of board
        """
        occupant = self.grid[row][col]
        if occupant == CELL_BLACK:
            return PLAYER_BLACK
        if occupant == CELL_RED:
            return PLAYER_RED
        else:
            return UNKNOWN

    def get_winner(self):
         return self.winner

    def is_winner(self, player):
        tile = CELL_BLACK if player == PLAYER_BLACK else CELL_RED

        # check horizontal spaces
        for row in range(self.rows):
            for col in range(self.cols - 4):
                """print ('check horizontal [%s,%s][%s,%s][%s,%s][%s,%s][%s,%s]' %(row, col, row, col+1, row, col+2, row, col+3, row, col+4))"""
                if self.grid[row][col] == tile and \
                   self.grid[row][col + 1] == tile and \
                   self.grid[row][col + 2] == tile and \
                   self.grid[row][col + 3] == tile and \
                   self.grid[row][col + 4] == tile:
                    return True

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
