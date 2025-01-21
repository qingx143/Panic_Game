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

# initialize sausages
saus1 = backhouseMain.Sausage(75, 75, 30, 250, (255, 0, 0))
saus2 = backhouseMain.Sausage(115, 75, 30, 250, (255, 0, 0))
saus3 = backhouseMain.Sausage(155, 75, 30, 250, (255, 0, 0))
saus4 = backhouseMain.Sausage(195, 75, 30, 250, (255, 0, 0))

running = True

while running:
    screen.fill('white')
    mouse = pygame.mouse.get_pos()

    backhouseMain.boilSausage(screen, saus1, saus2, saus3, saus4)

    # for loop through the event queue
    for event in pygame.event.get():
        # check for QUIT event
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        #if event.type == pygame.MOUSEBUTTONDOWN:
            #backhouseMain.boilSausage_clicks(screen, mouse, saus1)

        if event.type == pygame.MOUSEMOTION:
            backhouseMain.boilSausage_clicks(screen, mouse, saus1, saus2, saus3, saus4)

    pygame.display.update()
    clock.tick(60)
    