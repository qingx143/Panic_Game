import pygame
import sys
import backhouseMain

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
    mouse = pygame.mouse.get_pos()

    backhouseMain.dough(screen, mouse)

    # for loop through the event queue
    for event in pygame.event.get():
        # check for QUIT event
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            backhouseMain.dough_clicks(screen, mouse)

    pygame.display.update()
    clock.tick(60)
    