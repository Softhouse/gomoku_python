from events import *

UNKNOWN = ' '
PLAYER_BLACK = 'b'
PLAYER_RED = 'r'


class GameEngine(object):
    """
    Tracks the game state.
    (solutions/iteration_2)
    """

    def __init__(self, evManager, height, width):
        # Create a grid of given height (nr of rows) and width (nr of columns)
        self.width = width
        self.height = height
        self.grid = [[UNKNOWN for x in range(width)] for y in range(height)]
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
        if self.winner == UNKNOWN and self.is_valid_move(row, col):
            self.grid[row][col] = PLAYER_BLACK if self.player == PLAYER_BLACK else PLAYER_RED
            if self.is_winner(self.player):
                self.winner = self.player
            else:
                self._switch_player()
        self._debug_grid()

    def _debug_grid(self):
        """For debug purposes"""
        print('    %s' % range(self.width))
        for row in range(self.height):
            print(row, self.grid[row])

    def is_valid_move(self, row, col):
        """
        Return True if it is valid to move to cell row, col. You cannot move to an occupied cell
        on grid or to a cell outside grid.
        """
        try:
            result = self.grid[row][col] == UNKNOWN
        except IndexError:
            result = False
        return result

    def get_piece(self, row, col):
        """
        Return piece in row, col of board. Enables View to find out what to draw on GUI
        """
        return self.grid[row][col]

    def get_winner(self):
        """Return winner of the game, enables View to declare winner and take appropriate action"""
        return self.winner

    def is_winner(self, player):
        """Calculate if there is a winner or not. Check both colors and all combinations to determine this
        Return True iff there is a winner, else False"""
        tile = player

        # check horizontal spaces
        for row in range(self.height):
            for col in range(self.width - 4):
                """print ('check horizontal [%s,%s][%s,%s][%s,%s][%s,%s][%s,%s]' %(row, col, row, col+1, row, col+2, row, col+3, row, col+4))"""
                if self.grid[row][col] == tile and \
                                self.grid[row][col + 1] == tile and \
                                self.grid[row][col + 2] == tile and \
                                self.grid[row][col + 3] == tile and \
                                self.grid[row][col + 4] == tile:
                    return True

        # check vertical spaces
        for col in range(self.width):
            for row in range(self.height - 4):
                """print ('check vertical [%s,%s][%s,%s][%s,%s][%s,%s][%s,%s]' %(row, col, row+1, col, row+2, col, row+3, col, row+4, col))"""
                if self.grid[row][col] == tile and \
                                self.grid[row + 1][col] == tile and \
                                self.grid[row + 2][col] == tile and \
                                self.grid[row + 3][col] == tile and \
                                self.grid[row + 4][col] == tile:
                    return True

        # check / diagonal spaces
        for row in range(self.height - 4):
            for col in range(4, self.width):
                """print ('check / diagonal [%s,%s][%s,%s][%s,%s][%s,%s][%s,%s]' %(row, col, row+1, col-1, row+2, col-2, row+3, col-3, row+4, col-4))"""
                if self.grid[row][col] == tile and \
                                self.grid[row + 1][col - 1] == tile and \
                                self.grid[row + 2][col - 2] == tile and \
                                self.grid[row + 3][col - 3] == tile and \
                                self.grid[row + 4][col - 4] == tile:
                    return True

        # check \ diagonal spaces
        for row in range(self.height - 4):
            for col in range(self.width - 4):
                """print ('check \ diagonal [%s,%s][%s,%s][%s,%s][%s,%s][%s,%s]' %(row, col, row+1, col+1, row+2, col+2, row+3, col+3, row+4, col+4))"""
                if self.grid[row][col] == tile and \
                                self.grid[row + 1][col + 1] == tile and \
                                self.grid[row + 2][col + 2] == tile and \
                                self.grid[row + 3][col + 3] == tile and \
                                self.grid[row + 4][col + 4] == tile:
                    return True

        return False

    def notify(self, event):
        """
        Receive a notification.
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
