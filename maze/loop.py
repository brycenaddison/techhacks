import pygame
from maze.game import Game
from maze.interface import build
from maze.blocks import Canvas

clock = pygame.time.Clock()


def build_loop(window):
    all_sprites = pygame.sprite.Group()
    canvas = Canvas(all_sprites)
    while True:
        clock.tick(Game.fps)
        Game.check_quit()  # Checks if game is being quit, will close game if true.
        window.fill(Game.color)
        build(window, "Build Phase", outline_width=2)
        canvas.draw()
        all_sprites.draw(window)
        pygame.display.flip()
