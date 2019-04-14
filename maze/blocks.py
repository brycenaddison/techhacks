import pygame
from pygame.locals import *
from maze.game import Game
from maze.player import Player


class Block(pygame.sprite.Sprite):
    def __init__(self, coords, width=5, color=(0, 0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.coords = coords
        self.width = width
        self.color = color
        self.image = pygame.Surface((width, width))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = coords

    def get_coords(self):
        point = (int(self.coords[0]), int(self.coords[1]))
        return point


class Canvas:
    def __init__(self, width=Game.side, height=Game.side, x=0, y=0, block_width=3):
        self.width = width
        self.height = height
        self.block_width = block_width
        self.block_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.blocks = []
        self.running = False
        self.start_point = None
        self.window = pygame.Surface((int(self.width), int(self.height)))
        self.rect = self.window.get_rect()
        self.rect.x = int(x)
        self.rect.y = int(y)
        self.player = self.create_dummy()

    def create_player(self):
        player = Player(0, self.height/2-self.height/32, self.width, self.height, self.player_group,
                             self.block_group, width=self.height/16, height=self.height/16, color=(0, 0, 255))
        self.player_group.add(player)
        return player

    def move_player(self, direction):
        return self.player.move(direction)

    def create_dummy(self):
        player = Player(0, self.height / 2 - self.height / 32, self.width, self.height, self.player_group,
                             self.block_group, width=self.height / 16, height=self.height / 16, color=(100, 100, 100))
        self.player_group.add(player)
        return player

    def get_player_distances(self):
        pos = self.player.pos()
        xpos_dist = int(self.width - pos[0])
        xneg_dist = int(pos[0])
        ypos_dist = int(self.height - pos[1])
        yneg_dist = int(pos[1])
        for block in self.blocks:
            bpos = block.get_coords()
            if pos[0] == bpos[0]:
                if bpos[1] > pos[1] and bpos[1] - pos[1] < ypos_dist:
                    ypos_dist = bpos[1] - pos[1]
                elif bpos[1] <= pos[1] and pos[1] - bpos[1] < yneg_dist:
                    yneg_dist = pos[1] - bpos[1]
            elif pos[1] == bpos[1]:
                if bpos[0] > pos[0] and bpos[0] - pos[0] < xpos_dist:
                    xpos_dist = bpos[0] - pos[0]
                elif bpos[0] <= pos[0] and pos[0] - bpos[0] < xneg_dist:
                    xneg_dist = pos[0] - bpos[0]
        return xpos_dist, ypos_dist, xneg_dist, yneg_dist

    def run(self):  # Sets running to true
        self.start_point = None
        self.player_group.empty()
        self.player = self.create_player()
        self.running = True

    def stop(self):  # Sets running to false
        self.start_point = None
        self.player_group.empty()
        self.player = self.create_dummy()
        self.running = False

    def is_running(self):  # Returns running
        return self.running

    def clear(self):  # Clears all points
        self.start_point = None
        self.blocks = []
        self.block_group.empty()

    def mouse_pos(self):  # Returns altered mouse pos based on canvas location to prevent offset
        mouse_pos = pygame.mouse.get_pos()
        mouse_pos = (int(mouse_pos[0] - self.rect.x), int(mouse_pos[1] - self.rect.y))
        return mouse_pos

    def draw(self, window):  # Draws objects on canvas surface
        self.block_group.draw(self.window)
        self.player_group.draw(self.window)
        self.preview_line()
        window.blit(self.window, self.rect)

    def fill(self, color=Game.color):
        self.window.fill(color)

    def surface(self):  # Returns canvas surface
        return self.window

    def block_at_pos(self, coords):  # Returns true if there is a block at a given point
        for block in self.blocks:
            if block.get_coords == coords:
                return True
        return False

    def point_is_valid(self, point):  # Returns if given point is on canvas
        if not 0 <= point[0] <= self.width or not 0 <= point[1] <= self.height:
            return False
        return True

    @staticmethod
    def min_max(a, b):  # Returns the smaller and larger value of two given values
        if a < b:
            small = a
            large = b
        else:
            small = b
            large = a
        return small, large

    @staticmethod
    def line(start_point, end_point):  # Generates a list of tuples of coordinates of a line between two points
        # Initializes points in a line
        points = []
        # Creates aliases for point coordinates
        try:
            x1 = start_point[0]
            x2 = end_point[0]
            y1 = start_point[1]
            y2 = end_point[1]
        except TypeError:
            return points  # Returns no points if a point is invalid
        # Returns a single point if start point is the same as endpoint
        if start_point == end_point:
            points.append(start_point)
            return points
        # Avoids divide by 0 for veritcal lines, returns vertical line of points
        if x1 == x2:
            low, hi = Canvas.min_max(y1, y2)
            for y in range(low, hi):
                points.append((x1, y))
        # Creates line by iterating through x plane if slope is less than or equal to 1
        elif abs((y1 - y2) / (x1 - x2)) <= 1:
            def f(var):
                return ((y1 - y2) / (x1 - x2)) * (var - x1) + y1
            low, hi = Canvas.min_max(x1, x2)
            for x in range(low, hi):
                points.append((x, f(x)))
        # Creates line by iterating through y plane is slope is greater than 1
        else:
            def f(var):
                return ((x1 - x2) / (y1 - y2)) * (var - y1) + x1
            low, hi = Canvas.min_max(y1, y2)
            for y in range(low, hi):
                points.append((f(y), y))
        # Returns list of tuples with coordinates for points to create
        return points

    def update(self, event):
        # On mouse click, start drawing a line
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            self.start_point = self.mouse_pos()
        # On mouse lift, finalize line creation and create a line of points
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            start_point = self.start_point
            end_point = self.mouse_pos()
            # Iterates through points generated by line generator and creates a Block object for each point
            for point in Canvas.line(start_point, end_point):
                self.create_block(point)
            # Resets the line
            self.start_point = None

    def preview_line(self, color=(255, 0, 0)):
        if self.start_point is not None:
            pygame.draw.aaline(self.window, color, self.start_point, self.mouse_pos())

    def create_block(self, point):  # Creates a Block object with given coordinates and adds it to sprite group
        if self.point_is_valid(point) and not self.block_at_pos(point):
            block = Block(point, width=self.block_width*2)
            self.blocks.append(block)
            self.block_group.add(block)
            if self.player is not None:
                pygame.sprite.groupcollide(self.player_group, self.block_group, False, True)
        return False
