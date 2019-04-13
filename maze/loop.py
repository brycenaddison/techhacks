import pygame
from maze.game import Game
from maze.text import Text
from maze.gui import Gui

clock = pygame.time.Clock()


def loop(window):
    while True:
        clock.tick(Game.fps)
        Game.check_quit()  # Checks if game is being quit, will close game if true.
        window.fill(Game.color)
        Gui.build(window, outline_width=2)
        pygame.display.flip()
