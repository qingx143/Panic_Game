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

    def __init__(self, x, y, w, h, colour):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.colour = colour
    
    def show(self, screen):
        pygame.draw.rect(screen, self.colour, pygame.Rect(self.x, self.y, self.w, self.h), 0, 20)
        

def boilSausage(screen): #boil sausages in this screen
    screen.fill('blue')
    pygame.draw.circle(screen, white, (600, 350), 250) #pot
    pygame.draw.rect(screen, green, pygame.Rect(50, 50, 200, 300)) #sasuage case

    sausage1 = Sausage(75, 75, 30, 250, (255, 0, 0))
    sausage1.show(screen)
    sausage2 = Sausage(115, 75, 30, 250, (255, 0, 0))
    sausage2.show(screen)
    sausage3 = Sausage(155, 75, 30, 250, (255, 0, 0))
    sausage3.show(screen)
    sausage4 = Sausage(195, 75, 30, 250, (255, 0, 0))
    sausage4.show(screen)

    #if pygame.mouse.get_pressed()[0]

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
