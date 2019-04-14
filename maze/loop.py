import pygame
from maze.game import Game
from maze.interface import build
from maze.blocks import Canvas
import sys

clock = pygame.time.Clock()


def build_loop(window):
    # Initializes the list of sprites
    blocks = pygame.sprite.Group()
    # Initializes canvas, which holds all point values drawn
    canvas = Canvas(blocks,
                    width=Game.side * 3 / 4,
                    height=Game.side / 2,
                    x=Game.side / 8,
                    y=Game.side / 4)
    while True:
        # Sets max FPS
        clock.tick(Game.fps)
        # Sets background color
        window.fill(Game.color)
        # Sets background color for canvas
        canvas.fill()
        # Builds GUI
        build(window, "Build Phase", canvas, outline_width=5)
        # Calls events
        for event in pygame.event.get():
            # Closes program is quit is called
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Passes events to canvas update, which checks for mouse inputs
            canvas.update(event)
        # Closes the game if the escape key is pressed
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        # Draws canvas to window
        canvas.draw(window)
        # Updates display
        pygame.display.flip()
