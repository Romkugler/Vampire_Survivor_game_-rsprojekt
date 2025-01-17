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

# Upload images
grass = pg.image.load("assets/sprites/grass.png")

# Set up display
WIDTH, HEIGHT = 800, 800
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Vampire Survivor Game")

# Set up variables
grass_x = WIDTH / 2 - WIDTH
grass_y = HEIGHT / 2 - HEIGHT
# Set up the clock for a decent framerate
clock = pg.time.Clock()

# Main game loop
running = True
while running:

    ## Event loop (inputs) ##
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        grass_y += 5
    if keys[pg.K_s]:
        grass_y -= 5
    if keys[pg.K_a]:
        grass_x += 5
    if keys[pg.K_d]:
        grass_x -= 5
        

    ## Update everything ##


    ## Draw everything ##
    screen.fill((0, 0, 0))
    screen.blit(grass, (grass_x, grass_y))

    # Update the display
    pg.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit pg
pg.quit()
sys.exit()

