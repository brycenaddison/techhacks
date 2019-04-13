import pygame
from maze.game import Game


class Gui:

    @staticmethod
    def build(window, outline_width=1):
        __class__.rectangle(window,
                            width=Game.side*3/4,
                            height=Game.side/8,
                            x=Game.side/8,
                            y=Game.side/8,
                            outline_width=outline_width)
        __class__.rectangle(window,
                            width=Game.side*3/4,
                            height=Game.side/2+outline_width*2,
                            x=Game.side/8,
                            y=Game.side/4-outline_width,
                            outline_width=outline_width)
        __class__.rectangle(window,
                            width=Game.side*3/4,
                            height=Game.side/8,
                            x=Game.side/8,
                            y=Game.side*3/4,
                            outline_width=outline_width
                            )


    @staticmethod
    def rectangle(window,
                  width=Game.side/2,
                  height=Game.side/2,
                  x=0,
                  y=0,
                  color=(0, 0, 0),
                  outline=True,
                  outline_width=10,
                  inner_box_color=Game.color):
        surface = pygame.Surface((int(width), int(height)))
        surface.fill(color)
        if outline:
            if outline_width * 2 >= height:
                outline_width = height / 2
            if outline_width * 2 >= width:
                outline_width = width / 2
            inner_surface = pygame.Surface((int(width-(outline_width*2)), int(height-(outline_width*2))))
            inner_surface.fill(inner_box_color)
            surface.blit(inner_surface, (outline_width, outline_width))
        rect = surface.get_rect()
        rect.x = int(x)
        rect.y = int(y)
        window.blit(surface, rect)

