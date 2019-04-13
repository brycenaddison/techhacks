import pygame
from maze.loop import loop
from maze.game import Game

WINDOW_TITLE = "Game"

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption(WINDOW_TITLE)
    window = pygame.display.set_mode((Game.side, Game.side), pygame.NOFRAME)
    loop(window)
    pygame.quit()
    quit()

