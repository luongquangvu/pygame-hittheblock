import pygame

class HUD(object):
	"""Head up display"""

	def __init__(self):
		super(HUD, self).__init__()
		self.troll_number_gauge = None
		self.troll_bullet_gauge = None
