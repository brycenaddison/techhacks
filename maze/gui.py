import pygame
from maze.game import Game
from maze.text import Text


class Gui:

    @staticmethod
    def rectangle(window,
                  width=Game.side/2,
                  height=Game.side/2,
                  x=0,
                  y=0,
                  color=(0, 0, 0),
                  hover_color=None,
                  clicked=False,
                  on_click=None,
                  args=(),
                  outline=True,
                  outline_width=10,
                  inner_box_color=Game.color,
                  message=None,
                  size_ratio=7/8,
                  font_face=Game.font,
                  font_color=(255, 255, 255)
                  ):
        surface = pygame.Surface((int(width), int(height)))
        if hover_color is not None and \
                x <= pygame.mouse.get_pos()[0] <= x + width and \
                y <= pygame.mouse.get_pos()[1] <= y + height:
            surface.fill(hover_color)
        else:
            surface.fill(color)
        if on_click is not None and clicked and \
                x <= pygame.mouse.get_pos()[0] <= x + width and \
                y <= pygame.mouse.get_pos()[1] <= y + height:
            on_click(*args)
        if outline:
            if outline_width * 2 >= height:
                outline_width = height / 2
            if outline_width * 2 >= width:
                outline_width = width / 2
            inner_surface = pygame.Surface((int(width-(outline_width*2)),
                                            int(height-(outline_width*2))))
            inner_surface.fill(inner_box_color)
            surface.blit(inner_surface, (outline_width, outline_width))
        if message is not None:
            Text.display(surface, message,
                         font_size=height*size_ratio,
                         font_face=font_face,
                         color=font_color,
                         center_x=width/2+0.5,
                         center_y=height/2+0.5)
        rect = surface.get_rect()
        rect.x = int(x)
        rect.y = int(y)
        window.blit(surface, rect)
