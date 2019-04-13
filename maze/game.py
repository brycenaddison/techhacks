import pygame
import sys


class Game:
    width = 360  # Width of screen
    height = int(width * 16/9)  # Height of screen
    boundary = width / 18  # Margins of screen
    fps = 60  # Refresh rate of game

    @staticmethod
    def check_quit():  # Checks if the game should be closed due to input
        # Closes the game if the close button is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Closes the game if the escape key is pressed
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
