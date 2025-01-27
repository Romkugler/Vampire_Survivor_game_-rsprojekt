# Vampire Survivor game
#
# TODO
# ✅Make a ground 
# ✅Make a player 
# ✅Move things around
# ✅Make enemies
# ✅Make player attack
# Make player die

import pygame as pg
import random 

# Initialize Pygame
pg.init()

## Slime class ##
class Slime:
    def __init__(self, x, y, hit_timer=0, hit=False, death_timer=0, alive=True, facing="r", health=100):
        self.x = x 
        self.y = y
        self.facing = facing
        self.health = health
        self.alive = alive
        self.death_timer = death_timer
        self.hit = hit
        self.hit_timer = hit_timer
slimes = []

## Transforms sprtie ##
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

# Upload #
grass = pg.image.load("assets/sprites/grass.png")
player_idle = pg.image.load("assets/sprites/Player_Idle.png")
player_run = pg.image.load("assets/sprites/Player_Run.png")
player_attack = pg.image.load("assets/sprites/Player_Attack.png")
slime_run = pg.image.load("assets/sprites/Slime_Run.png")
slime_death = pg.image.load("assets/sprites/Slime_Death.png")

# Player sprites
player_size = 64
player_idle_sprites = load_sprite_sheet(player_idle, player_size, player_size)
player_idle = []
for i in range(len(player_idle_sprites)//4):
    player_idle.append(player_idle_sprites[i])

player_run_sprites = load_sprite_sheet(player_run, player_size, player_size)
player_run_w = []
player_run_a = []
player_run_s = []
player_run_d = []
for i in range(len(player_run_sprites)//4):
    player_run_s.append(player_run_sprites[i])
    player_run_a.append(player_run_sprites[i+8])
    player_run_d.append(player_run_sprites[i+16])
    player_run_w.append(player_run_sprites[i+24])

player_attack_sprites = load_sprite_sheet(player_attack, player_size, player_size)
player_attack_w = []
player_attack_a = []
player_attack_s = []
player_attack_d = []
for i in range(len(player_attack_sprites)//4):
    player_attack_s.append(player_attack_sprites[i])
    player_attack_a.append(player_attack_sprites[i+6])
    player_attack_d.append(player_attack_sprites[i+12])
    player_attack_w.append(player_attack_sprites[i+18])

# Slime sprites
slime_size = 64
slime_run_sprites = load_sprite_sheet(slime_run, slime_size, slime_size)
slime_run_r = []
slime_run_l = []
for i in range(len(slime_run_sprites)//4):
    slime_run_r.append(slime_run_sprites[i+18])
    slime_run_l.append(slime_run_sprites[i+12])

slime_death_sprites = load_sprite_sheet(slime_death, slime_size, slime_size)
slime_death = []
for i in range(len(slime_death_sprites)//4):
    slime_death.append(slime_death_sprites[i+10])


# Set up display
WIDTH, HEIGHT = 800, 800
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Vampire Survivor Game")

# Set up variables
grass_x = WIDTH / 2 - WIDTH
grass_y = HEIGHT / 2 - HEIGHT
tick = 0
slime_speed = 1
player_coords = (WIDTH/2 - (player_size*1.5), HEIGHT/2 - (player_size*1.5)) # 1.5 = player_size/2 + player_size
player_attacking = False
attackspeed = 8
attacktime = attackspeed*6
slime_health = 100
attack_range = 100
player_damage = 1

# Set up the clock for a decent framerate
clock = pg.time.Clock()

# Main game loop
running = True
while running:
    player_moving = "idle"

    ## Event loop (inputs) ##
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    keys = pg.key.get_pressed()

    speed = 5
    if keys[pg.K_w]:
        grass_y += speed
        player_moving = "w"
        for s in slimes:
            s.y += speed
    if keys[pg.K_s]:
        grass_y -= speed
        player_moving = "s"
        for s in slimes:
            s.y -= speed
    if keys[pg.K_a]:
        grass_x += speed
        player_moving = "a"
        for s in slimes:
            s.x += speed
    if keys[pg.K_d]:
        grass_x -= speed
        player_moving = "d"
        for s in slimes:
            s.x -= speed
    if keys[pg.K_SPACE]:
        player_attacking = True

    ## Update everything ##

    # Slime spawn #
    slime_amount = 5
    if len(slimes) != slime_amount:
        for i in range(slime_amount-len(slimes)):
            slime_spawnpos_x = random.randint(0, WIDTH)
            slime_spawnpos_y = random.randint(0, HEIGHT)
            s = Slime(slime_spawnpos_x, slime_spawnpos_y)
            s = slimes.append(s)

    # Slime movement #
    for s in slimes:
        if s.alive:
            direction_x = player_coords[0] - s.x
            direction_y = player_coords[1] - s.y
            distance = (direction_x**2 + direction_y**2) ** 0.5
            if distance != 0:
                direction_x /= distance
                direction_y /= distance
            s.x += slime_speed * direction_x
            s.y += slime_speed * direction_y
            if direction_x < 0:
                s.facing = "l"
            else:
                s.facing = "r"
    

    # Player attack #
    if player_attacking:
        for s in slimes:
            if s.alive:
                direction_x = player_coords[0] - s.x
                direction_y = player_coords[1] - s.y
                distance = (direction_x**2 + direction_y**2) ** 0.5
                if distance <= attack_range:
                    s.hit = True
        attacktime += 1
        if attacktime >= attackspeed*6:
            player_attacking = False
            attacktime = 0

    # Slime damage #
    for s in slimes:
        if s.hit == True:
            s.hit_timer = attacktime
            if s.hit_timer == 1:
                s.hit = False
                s.health -= player_damage
        if s.health <= 0:
            s.alive = False

    print(slimes[0].health,"health")
    print(slimes[0].hit,"hit")
    print(slimes[0].hit_timer,"hit timer")



    ## Draw everything ##
    screen.fill((0, 0, 0))
    for x in range(-1,1):
        for y in range(-1,1):
            screen.blit(grass, (grass_x%grass.get_width() + grass.get_width()*x, grass_y%grass.get_height() + grass.get_height()*y))

    # Slime #
    for s in slimes:
        if s.alive:
            if s.hit_timer in range(2,10):
                screen.blit(slime_death[2], (s.x, s.y))
            else:
                if s.facing == "l":
                    screen.blit(slime_run_l[(tick//10%6)], (s.x, s.y))
                else:
                    screen.blit(slime_run_r[(tick//10%6)], (s.x, s.y))


        else:
            screen.blit(slime_death[(s.death_timer//10%10)], (s.x, s.y))
            s.death_timer += 1
            if s.death_timer >= 100:
                slimes.remove(s)


    # Player #
    if player_moving == "w":
        if player_attacking:
            screen.blit(player_attack_w[(attacktime//attackspeed%6)], player_coords)
        else:
            screen.blit(player_run_w[(tick//10%8)], player_coords)
    elif player_moving == "a":
        if player_attacking:
            screen.blit(player_attack_a[(attacktime//attackspeed%6)], player_coords)
        else:
            screen.blit(player_run_a[(tick//10%8)], player_coords)
    elif player_moving == "s":
        if player_attacking:
            screen.blit(player_attack_s[(attacktime//attackspeed%6)], player_coords)
        else:
            screen.blit(player_run_s[(tick//10%8)], player_coords)
    elif player_moving == "d":
        if player_attacking:
            screen.blit(player_attack_d[(attacktime//attackspeed%6)], player_coords)
        else:
            screen.blit(player_run_d[(tick//10%8)], player_coords)
    else:
        if player_attacking:
            screen.blit(player_attack_s[(attacktime//attackspeed%6)], player_coords)
        else:
            screen.blit(player_idle[(tick//15%8)], player_coords)



    # Update the display
    pg.display.flip()

    # Cap the frame rate
    clock.tick(60)

    tick += 1
# Quit pg
pg.quit()

