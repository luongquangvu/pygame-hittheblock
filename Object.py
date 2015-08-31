import pygame
from Global import *

class Object(pygame.sprite.Sprite):
	"""This class represent object"""

	def __init__(self):
		super(Object, self).__init__()
		self.image = None
		self.rect = None
		self.type = None
		self.width = 0
		self.height = 0
		
	def init(self, type, colorkey, width = 0, height = 0, file_name = "", color = WHITE):
		self.type = type
		self.width = width
		self.height = height

		if (type == 'Image'):
			self.image = pygame.image.load(file_name).convert_alpha()
			self.image.set_colorkey(colorkey)
			
		elif (type == 'Circle' or type == 'Ellipse'):
			self.image = pygame.Surface([width, height])
			self.image.fill(colorkey)
			self.image.set_colorkey(colorkey)
			pygame.draw.ellipse(self.image, color, [0, 0, width, height])
			
		elif (type == 'Square' or type == 'Rectangle'):
			self.image = pygame.Surface([width, height])
			self.image.fill(color)
			
		else:
			return False
		
		self.rect = self.image.get_rect()
		
	def move(self, x, y):
		self.rect.x = x
		self.rect.y = y
		
	def rotate(self, angle):
		self.image = pygame.transform.rotate(self.image, angle)
		
	def scale(self, x, y):
		self.image = pygame.transform.scale(self.image, [self.rect.width * x, self.rect.height * y])

	def change_color(self, color):
		if (self.type == 'Circle' or type == 'Ellipse'):
			pygame.draw.ellipse(self.image, color, [0, 0, self.width, self.height])
			
		elif (self.type == 'Square' or type == 'Rectangle'):
			self.image.fill(color)

		else:
			return