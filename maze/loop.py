import pygame
from maze.game import Game
from maze.interface import build

clock = pygame.time.Clock()


def build_loop(window):
    while True:
        clock.tick(Game.fps)
        Game.check_quit()  # Checks if game is being quit, will close game if true.
        window.fill(Game.color)
        build(window, "Build Phase", outline_width=2)
        pygame.display.flip()
