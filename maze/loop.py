import pygame
from maze.game import Game
from maze.text import Text

clock = pygame.time.Clock()


def loop(window):
    while True:
        clock.tick(Game.fps)
        Game.check_quit()  # Checks if game is being quit, will close game if true.
        window.fill((255, 255, 255))
        Text.display(window, "woah")
        pygame.display.flip()
