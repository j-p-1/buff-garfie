import pygame, sys, time # import the needed modules

pygame.init() # Init Pygame

display = pygame.display.set_mode((800, 800)) # Create a 800 pixel by 800 pixel display window

pygame.display.set_caption("Buff Garfie") # Set window title

# Get garf images:
garf_a = pygame.image.load("GarfImages/garf1.jpg")
garf_b = pygame.image.load("GarfImages/garf2.jpg")
garf_c = pygame.image.load("GarfImages/garf3.jpg")
garf_d = pygame.image.load("GarfImages/garf4.jpg")

# Mainloop:

zoop = True

WAIT = 0.5

while zoop:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit() # Stop Pygame
			sys.exit() # Exit the window as after calling the above, the window with the content just hangs.
			
	display.blit(garf_a, (0, 0)) # Show garf image 1
	pygame.display.flip() # Show Garfie
	time.sleep(WAIT)
	display.blit(garf_b, (0, 0)) # Show garf image 2
	pygame.display.flip() # Show Garfie
	time.sleep(WAIT)
	display.blit(garf_c, (0, 0)) # Show garf image 3
	pygame.display.flip() # Show Garfie
	time.sleep(WAIT)
	display.blit(garf_d, (0, 0)) # Show garf image 4
	pygame.display.flip() # Show Garfie
	time.sleep(WAIT)
