import pygame
import os

# includes classes for button making, gifs, and mouse helper functions

# Buttons ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Button:
    """
    Creates an interactive button.
    Button(x, y, w, h, corner, base_colour)

    create_button(screen, mouse):
        Sets up the button.

    set_text(screen, text):
        sets the text (call this method before create_button())
    """
    x: float
    y: float
    w: float
    h: float
    corner: int
    base_colour: tuple[int, int, int]
    text: str

    def __init__(self, x, y, w, h, corner, base_colour):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.corner = corner
        self.base_colour = base_colour
        self.text = ''

    def set_text(self, screen, text):
        self.text = text

    def create_button(self, screen, mouse):
        button = pygame.Rect(self.x - self.w / 2, self.y - self.h / 2, self.w,
                             self.h)
        pygame.draw.rect(screen, self.base_colour, button, 0, self.corner)

        # adding text
        if self.text != '':
            pygame.font.init()
            path = os.path.join(os.getcwd(), 'Assets', 'TitleFont.ttf')
            title_font = pygame.font.Font(path, 20)
            text = title_font.render(self.text, False, (0, 0, 0))
            screen.blit(text, (self.x - self.w / 2 + 20, self.y - self.h / 5))

        # makes button tactile
        if mouse_tact(self.x, self.y, self.w, self.h, mouse):
            pygame.draw.rect(screen, (255, 255, 255), button, 3, self.corner)
            if self.text != '':
                text = title_font.render(self.text, False, (255, 255, 255))
            screen.blit(self.text, (self.x - self.w / 2 + 20, self.y - self.h / 5))


# GIF ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Gif():
    """
    Creates a gif (animation).
    Gif(x, y, w, h, num_of_frames, png_name)
        Note: please make sure png_name is in the format <name_i>, where i is
                    an integer from 0 to num_of_frames - 1

    show(screen, counter, x, y, player)
    Note: this is currently under construction.

    """
    x: float
    y: float
    w: float
    h: float
    speed: float
    frames: int
    images: list
    j: int

    def __init__(self, x, y, w, h, frames, png_type):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.images = []
        self.counter = 0
        self.j = 0
        for i in range(frames):
            im = pygame.transform.scale(pygame.image.load(
                os.path.join("Assets", f"{png_type} {i}.png")), (100, 100))
            self.images.append(im)

    def show(self, screen, counter, x, y, player):
        im = self.images[self.j]
        if player == 2:
            im = pygame.transform.flip(self.images[self.j], True, False)
        screen.blit(im, (x, y))
        if counter % 10 == 0:
            self.j += 1
        if self.j == len(self.images):
            self.j = 0

# mouse helper functions
def mouse_tact(x, y, w, h, mouse) -> bool:
    """
    Detects mouse movement on screen -> specifically checks if the mouse is
        currently within a rectangle.
    """
    if (x - w/2 <= mouse[0] <= x + w/2) and (y - h/2 <= mouse[1] <= y + h/2):
        return True
    return False

def mouse_click(x, y, w, h, newMode, mouse, mode) -> int:
    """
    Detects mouse clicks on a screen -> specifically if the mouse has clicked
        on a rectangle (then the mode will change from mode to newMode)
    """
    if (x - w/2 <= mouse[0] <= x + w/2) and (y - h/2 <= mouse[1] <= y + h/2):
        return newMode
    return mode
