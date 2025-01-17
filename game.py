# Vampire Survivor game
#
# TODO
# Make a ground
# Make a player 
# Move things around
# Make enemies
# Make player attack

import pygame as pg
import sys

# Initialize Pygame
pg.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Vampire Survivor Game")

# Set up the clock for a decent framerate
clock = pg.time.Clock()

# Main game loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Fill the screen with a color (RGB)
    screen.fill((0, 0, 0))

    # Update the display
    pg.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit pg
pg.quit()
sys.exit()

