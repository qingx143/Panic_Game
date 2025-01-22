import pygame

def front_house_layout(screen, x, y, w, h):
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

    character_movement(screen, x, y, w, h)

def character_movement(screen, player_x, player_y, player_w, player_h):
    player = pygame.Rect(player_x, player_y, player_w, player_h)
    pygame.draw.rect(screen, 'blue', player)

def is_touching_objects(x, y, w, h) -> str:
    # back wall
    if is_touching(x, y, w, h, 0, 0, 1000, 25):
        return is_touching_side(x, y, w, h, 0, 0, 1000, 25)

    # counters
    if is_touching(x, y, w, h, 0, 225, 575, 100):
        return is_touching_side(x, y, w, h, 0, 225, 575, 100)
    if is_touching(x, y, w, h, 0, 25, 100, 50):
        return is_touching_side(x, y, w, h, 0, 25, 100, 50)
    if is_touching(x, y, w, h, 250, 25, 375, 50):
        return is_touching_side(x, y, w, h, 250, 25, 375, 50)

    # tables
    if is_touching(x, y, w, h, 750, 170, 170, 140):
        return is_touching_side(x, y, w, h, 750, 170, 170, 140)
    if is_touching(x, y, w, h, 750, 440, 170, 140):
        return is_touching_side(x, y, w, h, 750, 440, 170, 140)

    return "NONE"

def is_touching(x, y, w, h, ox, oy, ow, oh) -> bool:
    if (x + w >= ox) and (x <= ox + ow) and (y + h >= oy) and (y <= oy + oh):
        return True
    return False

def is_touching_side(x, y, w, h, ox, oy, ow, oh) -> str:
    if x + w == ox:
        return "RIGHT"
    if x == ox + ow:
        return "LEFT"
    if y + h == oy:
        print("FDLSJFLKDJSFKLJDSKLFJKLDSJFKLDSJFKLJDSL")
        return "TOP"
    if y == oy + oh:
        return "BOTTOM"
    return "NONE"




