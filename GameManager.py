import pygame
from State import *

class GameManager(object):
	def __init__(self):
		super(GameManager, self).__init__()

		self.current_state = None
		#self.next_state = None

	def change_state(self, state):
		self.current_state = state
		self.current_state.init()

	def process_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True
			else:
				self.current_state.process_events(event)
		
		return False

	def update(self):
		#if (self.current_state != self.next_state):
		#	current_state = next_state

		self.current_state.update()

	def draw(self, screen):
		self.current_state.draw(screen)
		pygame.display.flip()