import pygame, sys # import the needed modules

pygame.init() # Init Pygame

display = pygame.display.set_mode((800, 800)) # Create a 800 pixel by 800 pixel display window

pygame.display.set_caption("Buff Garfie") # Set window title

# Mainloop:

zoop = True

while zoop:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit() # Stop Pygame
			sys.exit() # Exit the window as after calling the above, the window with the content just hangs.
