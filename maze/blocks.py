import pygame
from pygame.locals import *

class Block(pygame.sprite.Sprite):
    def __init__(self, coords, width=5, color=(0,0,0)):
        pygame.sprite.Sprite.__init__(self)
        self.coords = coords
        self.width = width
        self.color = color
        self.image = pygame.Surface((width, width))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = coords

    def get_coords(self):
        return self.coords

class Canvas:
    def __init__(self, all_sprites):
        self.all_sprites = all_sprites
        self.blocks = []
        self.drawing = False
        self.start_point = None

    def block_at_pos(self, coords):
        for block in self.blocks:
            if block.get_coords == coords:
                return True
        return False

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and not self.block_at_pos(mouse_pos):
            self.create_block(mouse_pos)

    def update(self, window, event, color=(255, 0, 0)):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            self.drawing = True
            self.start_point = pygame.mouse.get_pos()
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            self.drawing = False
            start_point = self.start_point
            end_point = pygame.mouse.get_pos()
            for point in Canvas.line(start_point, end_point):
                self.create_block(point)
            self.start_point = None
        if self.drawing:
            pygame.draw.line(window, color, self.start_point, pygame.mouse.get_pos())

    def create_block(self, point):
        block = Block(point)
        self.all_sprites.add(block)
'''
def draw(window):
    if event.type == MOUSEBUTTONDOWN and event.button == 1:



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
'''