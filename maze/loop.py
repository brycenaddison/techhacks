import pygame
from maze.game import Game

clock = pygame.time.Clock()

BLACK = (  0,   0,   0)

WHITE = (255, 255, 255)
RED = (255,   0,   0)

GREEN = (  0, 255,   0)

BLUE = (  0,   0, 255)
def loop(window):
    while True:
        clock.tick(Game.fps)
        Game.check_quit()  # Checks if game is being quit, will close game if true.
        window.fill((255, 255, 255))
        pygame.draw.rect(window,BLACK,(100,100,300,10))



        pygame.display.flip()
