from eventmanager import *


class GameEngine(object):
    """
    Tracks the game state.
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
        self.player = 'black'
        self.winner = ' '
        self.evManager = evManager
        evManager.RegisterListener(self)
        self.running = False

    def _switch_player(self):
        self.player = 'red' if self.player == 'black' else 'black'
        return self.player

    def get_next_player(self):
        """
        ...
        """
        return self.player

    def _set_piece(self, pos):
        row, col = pos
        if self.winner == ' ' and self.is_valid_move(row, col):
            self.grid[row][col] = 1 if self.player == 'black' else 2
            if self.is_winner(self.player):
                self.winner = self.player
            else:
                # Update next player
                self._switch_player()

        # debug
        print('    %s' % range(self.cols))
        for row in range(self.rows):
            print(row, self.grid[row])

    def is_valid_move(self, row, col):
        """
        ...
        """
        try:
            result = self.grid[row][col] == 0
        except IndexError:
            result = False
        return result

    def get_piece(self, row, col):
        """
        ...
        """
        occupant = self.grid[row][col]
        if occupant == 1:
            return 'black'
        if occupant == 2:
            return 'red'
        else:
            return ' '

    def get_winner(self):
        """
        ....
        """
        return self.winner

    def is_winner(self, player):
        """
        ...
        """
        tile = 1 if player == 'black' else 2

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

        # check vertical spaces
        for col in range(self.cols):
            for row in range(self.rows - 4):
                """print ('check vertical [%s,%s][%s,%s][%s,%s][%s,%s][%s,%s]' %(row, col, row+1, col, row+2, col, row+3, col, row+4, col))"""
                if self.grid[row][col] == tile and \
                   self.grid[row + 1][col] == tile and \
                   self.grid[row + 2][col] == tile and \
                   self.grid[row + 3][col] == tile and \
                   self.grid[row + 4][col] == tile:
                    return True

        # check / diagonal spaces
        for row in range(self.rows - 4):
            for col in range(4, self.cols):
                """print ('check / diagonal [%s,%s][%s,%s][%s,%s][%s,%s][%s,%s]' %(row, col, row+1, col-1, row+2, col-2, row+3, col-3, row+4, col-4))"""
                if self.grid[row][col] == tile and \
                   self.grid[row + 1][col - 1] == tile and \
                   self.grid[row + 2][col - 2] == tile and \
                   self.grid[row + 3][col - 3] == tile and \
                   self.grid[row + 4][col - 4] == tile:
                    return True

        # check \ diagonal spaces
        for row in range(self.rows - 4):
            for col in range(self.cols - 4):
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
        Called by an event in the message queue.
        """

        if isinstance(event, QuitEvent):
            self.running = False
        elif isinstance(event, MouseInputEvent):
            self._set_piece(event.clickpos)

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
