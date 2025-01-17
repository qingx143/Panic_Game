import pygame
import sys
from backhouseMain import boilSausage, frySausage, dough

# initializing game start
pygame.init()
clock = pygame.time.Clock()

# initializing screen
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

running = True

while running:
    screen.fill('white')
    dough(screen)
    mouse = pygame.mouse.get_pos()

    # for loop through the event queue
    for event in pygame.event.get():
        # check for QUIT event
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    pygame.display.update()
    clock.tick(60)
    