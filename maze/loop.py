import pygame
from maze.game import Game
from pygame.locals import *

clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
def loop(window):
    while True:
        clock.tick(60)
        Game.check_quit()  # Checks if game is being quit, will close game if true.
        window.fill((255, 255, 255))
        #pygame.draw.rect(window,black, [400, 300, 10, 10], 20)
        #pygame.draw.line(window, black, [200,200], [400,200], 10);
        checkShape(window)
        pygame.display.update()

def checkShape(screen):
    black, white = (0, 0, 0), (255, 255, 255)
    red, green, blue = (255, 0, 0), (0, 255, 0), (0, 0, 255)

    def draw_line(color, start, end):
        pygame.draw.line(screen, color, start, end, 10)
    def draw_square(color, start, end):
        width = end[0] - start[0]
        pygame.draw.rect(screen, color, (start[0], start[1], width, width))
    shapes = [[draw_square, white, (0, 0), (480, 480)]]
    shape, color, start = draw_line, black, None

    def draw_shapes():
        for shape in shapes:
            func, color, start, end = shape
            func(color, start, end)

    while True:
        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            start = pygame.mouse.get_pos()
            shapes.append([shape, color, start, start])
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            start = None
        if start is not None:
            shapes[-1][-1] = pygame.mouse.get_pos()

        draw_shapes()
        pygame.display.flip()
