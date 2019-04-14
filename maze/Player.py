class Player(pygame.sprite.Sprite):
	def _init_(self, x, y, width=10, height=10, color=(0, 0, 0))
		super()._init_()
		self.x = x
		self.y = y
		self.image = pygame.Surface((width, height))
		self.image.fill(color)


	def left(self):
		x = x-1
	
	def right(self):
		x = x+1

	def up(self):
		y = y-1

	def down(self):
		y = y+1

player = Player(0, 0)
player_group = pygame.sprite.Group()
player_group.add(player)
player_group.draw(window)

player_group.collide(block_group
