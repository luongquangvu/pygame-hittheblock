import os
import pygame
import random
from ResourceManager import *
from GameManager import *
from Scene import *
from Global import *

def main():
	# Create window at center
	os.environ['SDL_VIDEO_CENTERED'] = '1'

	# Initialize Pygame and set up the window
	pygame.init()

	size = [SCREEN_WIDTH, SCREEN_HEIGHT]
	screen = pygame.display.set_mode(size)
	
	pygame.mouse.set_visible(False)
	
	# Read resource
	ResourceManager.read_resources(RM_path)

	# Create an instance of the Game class
	game = GameManager()
	game.change_state(Scene())

	done = False
	clock = pygame.time.Clock()
	
	# Main game loop
	while not done:
		pygame.display.set_caption("Troll Shooting - FPS : " + str(round(clock.get_fps(), 1)))

		# Process events (keystrokes, mouse clicks, etc)
		done = game.process_events()
		
		# Update object positions, check for collisions
		game.update()
		
		# Draw the current frame
		game.draw(screen)
		
		# Pause for the next frame
		clock.tick(60)
		
	# Close window and exit
	pygame.quit()

if __name__ == "__main__":
	main()