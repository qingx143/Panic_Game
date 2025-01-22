import pygame
import sys

import front_house

# initializing game start
pygame.init()
clock = pygame.time.Clock()

# initializing screen
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

running = True

# initiating character keys
akey = False
wkey = False
skey = False
dkey = False
player_x = 420
player_y = 140
player_w = 50
player_h = 75

while running:
    screen.fill('white')
    mouse = pygame.mouse.get_pos()

    # character movement
    if akey and not front_house.is_touching_objects(player_x, player_y, player_w, player_h) == "RIGHT":
        player_x -= 1
    if dkey and not front_house.is_touching_objects(player_x, player_y, player_w, player_h) == "LEFT":
        player_x += 1
    if wkey and not front_house.is_touching_objects(player_x, player_y, player_w, player_h) == "UP":
        print(front_house.is_touching_objects(player_x, player_y, player_w, player_h))
        player_y -= 1
    if skey and not front_house.is_touching_objects(player_x, player_y, player_w, player_h) == "DOWN":
        player_y += 1

    front_house.front_house_layout(screen, player_x, player_y, player_w, player_h)

    # for loop through the event queue
    for event in pygame.event.get():
        # check for QUIT event
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                akey = True
            if event.key == pygame.K_w:
                wkey = True
            if event.key == pygame.K_s:
                skey = True
            if event.key == pygame.K_d:
                dkey = True
            if event.key == pygame.K_LEFT:
                akey = True
            if event.key == pygame.K_UP:
                wkey = True
            if event.key == pygame.K_DOWN:
                skey = True
            if event.key == pygame.K_RIGHT:
                dkey = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                akey = False
            if event.key == pygame.K_w:
                wkey = False
            if event.key == pygame.K_s:
                skey = False
            if event.key == pygame.K_d:
                dkey = False
            if event.key == pygame.K_LEFT:
                akey = False
            if event.key == pygame.K_UP:
                wkey = False
            if event.key == pygame.K_DOWN:
                skey = False
            if event.key == pygame.K_RIGHT:
                dkey = False

    pygame.display.update()
    clock.tick(60)
