import pygame

def front_house_layout(screen):
    screen.fill('grey')

    # back wall
    counter = pygame.Rect(0, 0, 1000, 25)
    pygame.draw.rect(screen, 'black', counter)

    # counters
    counter = pygame.Rect(0, 225, 575, 100)
    pygame.draw.rect(screen, 'black', counter)

    back_left_counter = pygame.Rect(0, 25, 100, 50)
    pygame.draw.rect(screen, 'black', back_left_counter)

    back_right_counter = pygame.Rect(250, 25, 375, 50)
    pygame.draw.rect(screen, 'black', back_right_counter)

    # tables
    pygame.draw.ellipse(screen, 'black', pygame.Rect(750, 170, 170, 140))
    pygame.draw.ellipse(screen, 'black', pygame.Rect(750, 440, 170, 140))
