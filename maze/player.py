import pygame


class Player(pygame.sprite.Sprite):
	def __init__(self, x, y, canvas_width, canvas_height, player_group, block_group,
				 width=10, height=10, color=(0, 0, 0)):
		pygame.sprite.Sprite.__init__(self)
		self.width = width
		self.height = height
		self.canvas_width = canvas_width
		self.canvas_height = canvas_height
		self.player_group = player_group
		self.block_group = block_group
		self.image = pygame.Surface((width, height))
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.tick = 0
		self.direction = 0

	def pos(self):
		pos = (int(self.rect.x), int(self.rect.y))
		return pos

	def move(self, direction, dist=1):
		if direction == 0:
			if self.rect.x + dist + self.width > self.canvas_width:
				self.rect.x = self.canvas_width - self.width
				return False
			else:
				self.rect.x = self.rect.x + dist
				x_dist = dist
				y_dist = 0
		elif direction == 2:
			if self.rect.x - dist < 0:
				self.rect.x = 0
				return False
			else:
				self.rect.x = self.rect.x - dist
				x_dist = -dist
				y_dist = 0
		elif direction == 1:
			if self.rect.y + dist + self.height > self.canvas_height:
				self.rect.y = self.canvas_height - self.height
				return False
			else:
				self.rect.y = self.rect.y + dist
				x_dist = 0
				y_dist = dist
		elif direction == 3:
			if self.rect.y + dist < 0:
				self.rect.y = 0
				return False
			else:
				self.rect.y = self.rect.y - dist
				x_dist = 0
				y_dist = -dist
		else:
			x_dist = 0
			y_dist = 0

		if len(pygame.sprite.groupcollide(self.player_group, self.block_group, False, False)) != 0:
			self.rect.x = self.rect.x - x_dist
			self.rect.y = self.rect.y - y_dist
			return False

		return True

	def update(self):
		if not self.move(self.direction):
			self.direction = self.direction + 1
			if self.direction > 3:
				self.direction = 0


