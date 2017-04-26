import pygame
import model
from events import *

BRIGHTBLUE = (0, 50, 255)
WHITE = (255, 255, 255)
BGCOLOR = BRIGHTBLUE
TEXTCOLOR = WHITE

WINDOWWIDTH = 640  # width of the program's window, in pixels
WINDOWHEIGHT = 480  # height in pixels
SPACESIZE = 50  # size of the tokens and individual board spaces in pixels

REDTOKENIMG = pygame.image.load('images/4row_red.png')
REDTOKENIMG = pygame.transform.smoothscale(REDTOKENIMG, (SPACESIZE, SPACESIZE))
BLACKTOKENIMG = pygame.image.load('images/4row_black.png')
BLACKTOKENIMG = pygame.transform.smoothscale(
    BLACKTOKENIMG, (SPACESIZE, SPACESIZE))
BOARDIMG = pygame.image.load('images/4row_board.png')
BOARDIMG = pygame.transform.smoothscale(BOARDIMG, (SPACESIZE, SPACESIZE))
NEXTPLAYERRECT = pygame.Rect(WINDOWWIDTH - int(3 * SPACESIZE / 2),
                             WINDOWHEIGHT - int(3 * SPACESIZE / 2), SPACESIZE, SPACESIZE)
WINNER_PLAYER_RECT = pygame.Rect(
    int(SPACESIZE * 7 / 2), WINDOWHEIGHT - int(3 * SPACESIZE / 2), SPACESIZE, SPACESIZE)
WINNER_MESSAGE_RECT = pygame.Rect(
    int(SPACESIZE / 2), WINDOWHEIGHT - int(3 * SPACESIZE / 3), SPACESIZE, SPACESIZE)
FRAMERATE = 30  # limit the redraw speed to 30 frames per second

TOKEN_RED = model.PLAYER_RED
TOKEN_BLACK = model.PLAYER_BLACK

class GraphicalView(object):
    """
    Draws the model state onto the screen.
    """

    def __init__(self, evManager, model, cols, rows):
        """
        evManager (EventManager): Allows posting messages to the event queue.
        model (GameEngine): a strong reference to the game Model.
        """

        self.evManager = evManager
        evManager.RegisterListener(self)
        self.model = model
        self.isinitialized = False
        self.screen = None
        self.clock = None
        self.smallfont = None
        self.boardWidth = cols
        self.boardHeight = rows
        self.x_margin = int((WINDOWWIDTH - cols * SPACESIZE) / 2)
        self.y_margin = int((WINDOWHEIGHT - rows * SPACESIZE) / 2)

    def notify(self, event):
        """
        Receive events posted to the message queue.
        """

        if isinstance(event, InitializeEvent):
            self.initialize()
        elif isinstance(event, QuitEvent):
            # shut down the pygame graphics
            self.isinitialized = False
            pygame.quit()
        elif isinstance(event, TickEvent):
            self.renderall()
            self.clock.tick(FRAMERATE)

    def renderall(self):
        """
        Draw the current game state on screen.
        Does nothing if isinitialized == False (pygame.init failed)
        """

        if not self.isinitialized:
            return
        # clear display
        self.screen.fill(BGCOLOR)
        # draw the board
        self.drawBoard()
        # flip the display to show whatever we drew
        pygame.display.flip()

    def drawBoard(self):
        # draw tokens
        spaceRect = pygame.Rect(0, 0, SPACESIZE, SPACESIZE)
        for x in range(self.boardWidth):
            for y in range(self.boardHeight):
                spaceRect.topleft = (
                    self.x_margin + (x * SPACESIZE), self.y_margin + (y * SPACESIZE))
                if self.model.get_piece(y, x) == TOKEN_BLACK:
                    self.screen.blit(BLACKTOKENIMG, spaceRect)
                elif self.model.get_piece(y, x) == TOKEN_RED:
                    self.screen.blit(REDTOKENIMG, spaceRect)

        # draw board over the tokens
        for x in range(self.boardWidth):
            for y in range(self.boardHeight):
                spaceRect.topleft = (
                    self.x_margin + (x * SPACESIZE), self.y_margin + (y * SPACESIZE))
                self.screen.blit(BOARDIMG, spaceRect)

        # draw the next player up
        player = BLACKTOKENIMG if self.model.get_next_player() == TOKEN_BLACK else REDTOKENIMG
        self.screen.blit(player, NEXTPLAYERRECT)

        # draw the winner
        winner_message = self.smallfont.render(
            'Winner is: ',
            True,
            (0, 255, 0))
        self.screen.blit(winner_message, WINNER_MESSAGE_RECT)
        if self.model.get_winner() != ' ':
            winner = BLACKTOKENIMG if self.model.get_winner() == TOKEN_BLACK else REDTOKENIMG
            self.screen.blit(winner, WINNER_PLAYER_RECT)

    def convert_mousepos(self, pos):
        """ convert window (x, y) coords into game field (row, col) values. """
        tokenx, tokeny = pos
        row = int((tokenx - self.x_margin) / SPACESIZE)
        column = int((tokeny - self.y_margin) / SPACESIZE)
        return column, row

    def initialize(self):
        """
        Set up the pygame graphical display and loads graphical resources.
        """
        result = pygame.init()
        pygame.font.init()
        pygame.display.set_caption('gomoku TDD')
        self.screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        self.clock = pygame.time.Clock()
        self.smallfont = pygame.font.Font(None, 40)
        self.isinitialized = True
