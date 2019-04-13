import pygame
from maze.loop import loop

WINDOW_TITLE = "Game"
X_DIMENSION = 600
Y_DIMENSION = 600

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption(WINDOW_TITLE)
    window = pygame.display.set_mode((X_DIMENSION, Y_DIMENSION))
    loop(window)
    pygame.quit()
    quit()
