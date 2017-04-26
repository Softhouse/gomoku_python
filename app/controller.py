import pygame

from events import *


class UserInput(object):
    """
    Handles keyboard and mouse input.
    """

    def __init__(self, evManager, view):
        """
        evManager (EventManager): Allows posting messages to the event queue.
        view (GraphicalView): a strong reference to the game view.
        """
        self.evManager = evManager
        evManager.RegisterListener(self)
        self.view = view

    def notify(self, event):
        """
        Receive events posted to the message queue.
        """
        if isinstance(event, TickEvent):
            # Called for each game tick.
            for event in pygame.event.get():
                # handle window manager closing our window
                if event.type == pygame.QUIT:
                    self.evManager.Post(QuitEvent())
                # handle key down events
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.evManager.Post(QuitEvent())
                    else:
                        # post any other keys to the message queue for everyone
                        # else to see
                        self.evManager.Post(KeyboardInputEvent(event.key))
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button:
                        row, col = self.view.convert_mousepos(event.pos)
                        self.evManager.Post(MouseInputEvent((row, col)))
