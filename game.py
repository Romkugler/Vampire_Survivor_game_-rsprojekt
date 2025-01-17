# Vampire Survivor game
#
# TODO
# ✅Make a ground 
# ✅Make a player 
# ✅Move things around
# Make enemies
# Make player attack
# Noice map

import pygame as pg
import sys

# Initialize Pygame
pg.init()

# Upload images
def load_sprite_sheet(sheet, sprite_width, sprite_height):
    sheet_rect = sheet.get_rect()
    sprites = []
    for y in range(0, sheet_rect.height, sprite_height):
        for x in range(0, sheet_rect.width, sprite_width):
            rect = pg.Rect(x, y, sprite_width, sprite_height)
            image = sheet.subsurface(rect)
            image = pg.transform.scale(image, (sprite_width * 3, sprite_height * 3))
            sprites.append(image)
    return sprites

grass = pg.image.load("assets/sprites/grass.png")
player_idle = pg.image.load("assets/sprites/Player_Idle.png")
player_run = pg.image.load("assets/sprites/Player_Run.png")

player_size = 64
player_idle_sprites = load_sprite_sheet(player_idle, player_size, player_size)
player_idle = []
for i in range(int(len(player_idle_sprites)/4)):
    player_idle.append(player_idle_sprites[i])

player_run_sprites = load_sprite_sheet(player_run, player_size, player_size)
player_run_w = []
player_run_a = []
player_run_s = []
player_run_d = []
for i in range(int(len(player_run_sprites)/4)):
    player_run_s.append(player_run_sprites[i])
    player_run_a.append(player_run_sprites[i+8])
    player_run_d.append(player_run_sprites[i+16])
    player_run_w.append(player_run_sprites[i+24])



# Set up display
WIDTH, HEIGHT = 800, 800
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Vampire Survivor Game")

# Set up variables
grass_x = WIDTH / 2 - WIDTH
grass_y = HEIGHT / 2 - HEIGHT
tick = 0

# Set up the clock for a decent framerate
clock = pg.time.Clock()

# Main game loop
running = True
while running:
    moving = "idle"

    ## Event loop (inputs) ##
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        keys = pg.key.get_pressed()
    speed = 3
    if keys[pg.K_w]:
        grass_y += speed
        moving = "w"
    if keys[pg.K_s]:
        grass_y -= speed
        moving = "s"
    if keys[pg.K_a]:
        grass_x += speed
        moving = "a"
    if keys[pg.K_d]:
        grass_x -= speed
        moving = "d"

    ## Update everything ##

    ## Draw everything ##
    screen.fill((0, 0, 0))
    screen.blit(grass, (grass_x, grass_y))
    if moving == "w":
        screen.blit(player_run_w[(tick//10%8)], (WIDTH / 2-player_size, HEIGHT / 2-player_size))
    elif moving == "a":
        screen.blit(player_run_a[(tick//10%8)], (WIDTH / 2-player_size, HEIGHT / 2-player_size))
    elif moving == "s":
        screen.blit(player_run_s[(tick//10%8)], (WIDTH / 2-player_size, HEIGHT / 2-player_size))
    elif moving == "d":
        screen.blit(player_run_d[(tick//10%8)], (WIDTH / 2-player_size, HEIGHT / 2-player_size))
    else:
        screen.blit(player_idle[(tick//15%8)], (WIDTH / 2-player_size, HEIGHT / 2-player_size))

    # Update the display
    pg.display.flip()

    # Cap the frame rate
    clock.tick(60)

    tick += 1
# Quit pg
pg.quit()
sys.exit()

