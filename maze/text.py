import pygame
from maze.game import Game


class Text:

    @staticmethod
    def display(window, message,
                font_size=Game.side/10,
                font_face=Game.font,
                center_x=Game.side/2,
                center_y=Game.side/2):  # Displays text on the screen
        font = pygame.font.Font(font_face, int(font_size))
        text_surface = font.render(message, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (center_x, center_y)
        window.blit(text_surface, text_rect)
