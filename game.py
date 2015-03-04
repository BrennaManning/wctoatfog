
import pygame, sys
from pygame.locals import *
# set up pygame
pygame.init()
# set up the window


"""

class Character():
    def __init__(self,pos_x,pos_y):
    
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.v_x = 50
        self.v_y = 0
        # TODO: don't depend on relative path
        self.image = pygame.image.load('images/char1.png')
        self.image.set_colorkey((255,255,255))
    def get_drawables(self):
        
        return [DrawableSurface(self.image, self.image.get_rect().move(self.pos_x, self.pos_y))]

    def update(self, delta_t):
        self.pos_x += self.v_x*delta_t
        self.pos_y += self.v_y*delta_t
        self.v_y += delta_t*100 # this is gravity in pixels / s^2

    def up(self):   
        self.v_y -= 1
"""
clock = pygame.time.Clock()

# run the game loop

lead_x = 300
lead_y = 300
vx = 0 
vy = 0


while True:
    for event in pygame.event.get():
        print event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


        if event.type == pygame.KEYDOWN:
            speed = 10
            if event.key == pygame.K_LEFT:
                vx = -speed
                vy = 0
            elif event.key == pygame.K_RIGHT:
                vx  = speed
                vy = 0
            elif event.key == pygame.K_UP:
                vx = 0
                vy = -speed
            elif event.key == pygame.K_DOWN:
                vx = 0
                vy = speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                vx = 0
                vy = 0

    lead_x += vx
    lead_y += vy
    windowSurface = pygame.display.set_mode((500, 400), 0, 32)

    # set up the colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    DARKBLUE = (0, 0, 83)
    PURPLE = (102, 51, 102)

    windowSurface.fill(DARKBLUE)

    pygame.draw.rect(windowSurface, PURPLE, [0, 0, 500, 20])
    pygame.draw.rect(windowSurface, PURPLE, [0, 0, 20, 180])
    pygame.draw.rect(windowSurface, PURPLE, [0, 220, 20, 180])
    pygame.draw.rect(windowSurface, PURPLE, [480, 0, 20, 180])
    pygame.draw.rect(windowSurface, PURPLE, [480, 220, 20, 180])
    pygame.draw.rect(windowSurface, PURPLE, [0, 380, 500, 20])

    pygame.draw.rect(windowSurface, GREEN, [lead_x, lead_y, 10, 10])
    #self.image = pygame.image.load('images/char1.png')
    #self.image.set_colorkey((255,255,255))
    pygame.display.update()
    #clock.tick(60)

        
