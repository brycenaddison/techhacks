import pygame, sys
import pygame, sys
from pygame.locals import *
from maze.loop import loop

WINDOW_TITLE = "Game"
X_DIMENSION = 600
Y_DIMENSION = 600

BLACK = (  0,   0,   0)

WHITE = (255, 255, 255)
RED = (255,   0,   0)

GREEN = (  0, 255,   0)

BLUE = (  0,   0, 255)

#if __name__ == "__main__":
pygame.init()
pygame.display.set_caption(WINDOW_TITLE)
window = pygame.display.set_mode((X_DIMENSION, Y_DIMENSION))
loop(window)
pygame.draw.rect(window,RED,(600,600,2,20))
pygame.quit()
quit()
