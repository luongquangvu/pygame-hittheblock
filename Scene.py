import pygame
from ResourceManager import *
from Global import *
from Player import *
from HUD import *
from State import *

class Scene(State):
	def __init__(self):
		super(Scene, self).__init__()

		self.all_object_list = pygame.sprite.Group()
		self.troll_list = pygame.sprite.Group()
		self.bullet_list = pygame.sprite.Group()
		self.player = Player()
		self.background = Object()
		self.hud = HUD()
		self.score = 0
		self.game_over = False

	def init(self):
		self.read_scene()

		# Scale background to screen size
		self.background.image = pygame.transform.scale(self.background.image, (SCREEN_WIDTH, SCREEN_HEIGHT))

		# TEST
		#self.player = Player()
		#self.player.init(type = 'Circle', colorkey = WHITE, width = 50, height = 50, color = RED)
		#self.all_object_list.add(self.player)

	def process_events(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			return
			#self.player.change_color(BLUE)
		elif event.type == pygame.KEYDOWN:
			if (event.ket == pygame.K_p):
				self.pause()

	def update(self):
		if (not self.is_running):
			return

		# TEST
		pos = pygame.mouse.get_pos()
		self.player.rect.x = pos[0]
		self.player.rect.y = pos[1]

	def draw(self, screen):
		screen.fill(WHITE)
		screen.blit(self.background.image, self.background.rect)
		self.all_object_list.draw(screen)

	def read_scene(self):
		with open(ResourceManager.scene_path_list[0]) as file:
			self.read_background(file)
			self.read_player(file)

	def read_background(self, file):
		file.readline()
		image_id = int(file.readline().strip().split(' ')[1])
		self.background.init('Image', None, file_name = ResourceManager.image_path_list[image_id])

	def read_player(self, file):
		file.readline()
		image_id = int(file.readline().strip().split(' ')[1])
		self.player.init('Image', None, file_name = ResourceManager.image_path_list[image_id])
		self.player.move(*map(int, file.readline().strip().split(' ')[1:]))
		self.player.rotate(float(file.readline().strip().split(' ')[1]))
		self.player.scale(*map(int, file.readline().strip().split(' ')[1:]))
		self.all_object_list.add(self.player)