import pygame
from maze.game import Game
from maze.interface import build
from maze.blocks import Canvas
import sys

clock = pygame.time.Clock()


def build_loop(window):
    # Initializes canvas, which holds all point values drawn
    canvas = Canvas(width=Game.side * 3 / 4,
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
        # Calls events
        clicked = False
        for event in pygame.event.get():
            # Closes program is quit is called
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked = True
            # Passes events to canvas update, which checks for mouse inputs
            canvas.update(event)
        # Closes the game if the escape key is pressed
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        # Builds GUI
        build(window, "Build Phase", "Not Running", canvas, clicked=clicked, outline_width=5)
        # Draws canvas to window
        canvas.draw(window)
        # Updates display
        pygame.display.flip()
        # Breaks loop if run button is clicked
        if canvas.is_running():
            run_loop(window, canvas)


def run_loop(window, canvas):
    while True:
        # Sets max FPS
        clock.tick(Game.fps)
        # Sets background color
        window.fill(Game.color)
        # Sets background color for canvas
        canvas.fill()
        # Checks if player hit goal
        canvas.hit_detect()
        # Calls events
        clicked = False
        for event in pygame.event.get():
            # Closes program is quit is called
            if event.type == pygame.QUIT:
                canvas.stop()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked = True
        # Closes the game if the escape key is pressed
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        # Player interpreter instead of failed AI
        if key[pygame.K_LEFT]:
            canvas.move_player(2)
        if key[pygame.K_RIGHT]:
            canvas.move_player(0)
        if key[pygame.K_UP]:
            canvas.move_player(3)
        if key[pygame.K_DOWN]:
            canvas.move_player(1)
        # Builds GUI
        build(window, "Running", "No AI Implemented D:", canvas, clicked=clicked, outline_width=5, running=True)
        # Draws canvas to window
        canvas.draw(window)
        # Updates display
        pygame.display.flip()
        # Breaks running loop if cancel button is clicked
        if not canvas.is_running():
            break
