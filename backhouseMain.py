import pygame

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
yellow = (120, 0, 0)
gray = (128, 128, 128)

class Sausage:
    x: float
    y: float
    w: float
    h: float
    colour: tuple[int, int, int]
    # rect  = pygame.Rect(self.x, self.y, self.w, self.h)

    def __init__(self, x, y, w, h, colour):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.colour = colour
        self.rect  = pygame.Rect(self.x, self.y, self.w, self.h)

    
    def show(self, screen):
        pygame.draw.rect(screen, self.colour, pygame.Rect(self.x, self.y, self.w, self.h), 0, 20)

    def update(self, x, y):
        #self.x = x
        #self.y = y
        # self.hover = self.rect.collidepoint(pygame.mouse.get_pos())
        # if self.hover is True:
        #     print(f'sausage at {saus1x}, {saus1y}')
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.x = x
            self.y = y
            print('poop')
        print(self.x, self.y)





def boilSausage_clicks(screen, mouse, saus1, saus2, saus3, saus4):
    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        # if x <= 90 and x >= 60:
        # saus1.update(x - 15, y - 125)
        # elif x <= 130 and x >= 100:
        # saus2.update(x - 15, y - 125)
        # elif x <= 170 and x >= 140:
        # saus3.update(x - 15, y - 125)
        # elif x <= 210 and x >= 180:
        saus4.update(x - 15, y - 125)


def boilSausage(screen, saus1, saus2, saus3, saus4): #boil sausages in this screen
    screen.fill('blue')
    pygame.draw.circle(screen, white, (600, 350), 250) #pot
    pygame.draw.rect(screen, green, pygame.Rect(50, 50, 200, 300)) #sasuage case

    saus1.show(screen)
    saus2.show(screen)
    saus3.show(screen)
    saus4.show(screen)
    # sausage1 = Sausage(saus1x, saus1y, 30, 250, (255, 0, 0))
    # sausage1.show(screen)
    # sausage2 = Sausage(saus2x, saus2y, 30, 250, (255, 0, 0))
    # sausage2.show(screen)
    # sausage3 = Sausage(saus3x, saus3y, 30, 250, (255, 0, 0))
    # sausage3.show(screen)
    # sausage4 = Sausage(saus4x, saus4y, 30, 250, (255, 0, 0))
    # sausage4.show(screen)


def frySausage(screen, mouse): #fry sausage
    screen.fill('green')
    pygame.draw.circle(screen, gray, (700, 350), 250) #pan
    pygame.draw.circle(screen, white, (220, 250), 200) #plate of sausages
    #pygame.transform.rotate(image, angle) //i'll make the pictures of the sausages tilted so it looks randomly put onto the plate

def dough(screen, mouse): #divide dough and roll dough into strip then roll into a strand
    screen.fill(red)

def dough_clicks(screen, mouse):
    pass
    
    #pygame.draw.rect(screen, green, pygame.Rect(50, 50, 200, 300)) #
