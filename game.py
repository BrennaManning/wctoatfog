""" This is W.C. Toatfog! We (Brenna and Joe) made this.
    You control the titular character, W.C. Toatfog, and you avoid the ghosts.
    They kill you. Have fun! """
import pygame, sys
import time
from pygame.locals import *
import random

# set up pygame
pygame.init()
pygame.mixer.init()

font = pygame.font.SysFont(None, 32)
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
speed = 500

class Model():
    """ Our model """
    def __init__(self,width,height):
        """ Initialize"""
        self.width = width
        self.height = height
        self.wc = WC(width/2, height/2)
        self.background = Background(width, height)
        self.obstacles = []
        self.enemy1 = Enemy(width/4, height/4)
        self.enemy2 = Enemy(3*width/4, height/4)
        self.enemy3 = Enemy(width/4, 3*height/4)
        self.enemy4 = Enemy(3*width/4, 3*height/4)

    def get_drawables(self):
        """ Return a list of DrawableSurfaces for the model """
        drawables = self.background.get_drawables()+self.wc.get_drawables()+self.enemy1.get_drawables()+self.enemy2.get_drawables()+self.enemy3.get_drawables()+self.enemy4.get_drawables()
        for obstacle in self.obstacles:
            drawables += obstacle.get_drawables()
        return drawables

    def get_player(self):
        """ returns the amazing W.C. Toatfog """
        return self.wc

    def is_dead(self):
        """ Return True if the player is dead (for instance) the player
            has collided with an obstacle, and false otherwise """
        if self.wc.pos_x + 10 > self.enemy1.pos_x -10 and self.wc.pos_x -10 < self.enemy1.pos_x + 10 and self.wc.pos_y + 10 > self.enemy1.pos_y -10 and self.wc.pos_y -10 < self.enemy1.pos_y +10:# and self.wc.pos_y > self.enemy1.pos_y + 13 and self.wc.pos_y < self.enemy1.pos_y - 13 : 
                return True
        if self.wc.pos_x + 10 > self.enemy2.pos_x -10 and self.wc.pos_x -10 < self.enemy2.pos_x + 10 and self.wc.pos_y + 10 > self.enemy2.pos_y -10 and self.wc.pos_y -10 < self.enemy2.pos_y +10:# and self.wc.pos_y > self.enemy1.pos_y + 13 and self.wc.pos_y < self.enemy1.pos_y - 13 : 
                return True
        if self.wc.pos_x + 10 > self.enemy3.pos_x -10 and self.wc.pos_x -10 < self.enemy3.pos_x + 10 and self.wc.pos_y + 10 > self.enemy3.pos_y -10 and self.wc.pos_y -10 < self.enemy3.pos_y +10:# and self.wc.pos_y > self.enemy1.pos_y + 13 and self.wc.pos_y < self.enemy1.pos_y - 13 : 
                return True
        if self.wc.pos_x + 10 > self.enemy4.pos_x -10 and self.wc.pos_x -10 < self.enemy4.pos_x + 10 and self.wc.pos_y + 10 > self.enemy4.pos_y -10 and self.wc.pos_y -10 < self.enemy4.pos_y +10:# and self.wc.pos_y > self.enemy1.pos_y + 13 and self.wc.pos_y < self.enemy1.pos_y - 13 : 
                return True
        else:
            return False 

    def update(self, dt):
        """ Updates model and such """
        self.wc.update(dt)
        self.enemy1.update(dt)
        self.enemy2.update(dt)
        self.enemy3.update(dt)
        self.enemy4.update(dt)

class DrawableSurface():
    """ Is any drawable surface """
    def __init__(self, surface, rect):
        """ Initialize drawable surface """
        self.surface = surface
        self.rect = rect

    def get_surface(self):
        """ Get the surface """
        return self.surface

    def get_rect(self):
        """ Get wrecked """
        return self.rect

class Background():
    """ Makes the background look fabulous """
    def __init__(self, screen_width, screen_height):
        """ Initialize the fabulous background """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.tile = pygame.image.load('images/stonetile.png')
        
    def get_drawables(self):
        """ get the drawables """
        drawables = []

        r1 = pygame.Rect(0,
                        self.screen_height-self.tile.get_rect().height,
                        self.tile.get_rect().width,
                        self.tile.get_rect().height)
        r2 = pygame.Rect(self.screen_width-self.tile.get_rect().width,
                        self.screen_height-self.tile.get_rect().height,
                        self.tile.get_rect().width,
                        self.tile.get_rect().height)
        r3 = pygame.Rect(0,
                        self.screen_height-self.tile.get_rect().height,
                        self.tile.get_rect().width,
                        self.tile.get_rect().height)
        r4 = pygame.Rect(0,
                        0,
                        self.tile.get_rect().width,
                        self.tile.get_rect().height)

        for i in range(17):
            drawables.append(DrawableSurface(self.tile,r1))
            r1 = r1.move(self.tile.get_rect().width,0)
            drawables.append(DrawableSurface(self.tile,r2))
            r2 = r2.move(0,-self.tile.get_rect().height)
            drawables.append(DrawableSurface(self.tile,r3))
            r3 = r3.move(0,-self.tile.get_rect().height)
            drawables.append(DrawableSurface(self.tile,r4))
            r4 = r4.move(self.tile.get_rect().width,0)

        r = [pygame.Rect(0, 0, 30, 24), pygame.Rect(0, 0, 20, 180), pygame.Rect(0, 220, 20, 180), 
                        pygame.Rect(480, 0, 20, 180), pygame.Rect(480, 220, 20, 180), pygame.Rect(0, 380, 500, 20)]

        for rect in r:
            drawables.append(DrawableSurface(self.tile, rect))
        
        return drawables

class WC():
    """ W.C. Toatfog comes to life! """
    def __init__(self,pos_x,pos_y):
        """ Initialize the sir and/or madam W.C. Toatfog """
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.v_x = 0
        self.v_y = 0
        self.image = pygame.image.load('images/char1.png')
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()

    def get_drawables(self):
        """ Get the picture of W.C. Toatfog """
        return [DrawableSurface(self.image, self.image.get_rect().move(self.pos_x, self.pos_y))]

    def update(self, delta_t):
        """ Update the position """
        self.pos_x += self.v_x*delta_t
        self.pos_y += self.v_y*delta_t

class Enemy():
    """ The enemies are such jerkfaces """
    def __init__(self,pos_x,pos_y):
        """ Initialize enemy """
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.v_x = random.randint(50,100)*((2*random.randint(0,1)-1))
        self.v_y = random.randint(50,100)*((2*random.randint(0,1)-1))
        self.image = pygame.image.load('images/enemy.png')
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()

    def get_drawables(self):
        """ Get the picture of the enemy """
        return [DrawableSurface(self.image, self.image.get_rect().move(self.pos_x, self.pos_y))]

    def update(self, delta_t):
        """ Update the position """
        if self.pos_x < 30:
            self.v_x = 10+abs(self.v_x)
        elif self.pos_x > 445:
            self.v_x = -10-abs(self.v_x)
        elif self.pos_y < 24:
            self.v_y = 10+abs(self.v_y)
        elif self.pos_y > 351:
            self.v_y = -10-abs(self.v_y)
        self.pos_x += self.v_x*delta_t
        self.pos_y += self.v_y*delta_t

class View():
    """ Our view of things """
    def __init__(self, model, width, height):
        """ Initialize view """
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.screen_boundaries = pygame.Rect(0,0,width,height)
        self.model = model
        self.counting_seconds = 0

    def draw(self):
        """ Redraw the game window """
        self.screen.fill((0,0,83))
        self.drawables = self.model.get_drawables()
        for d in self.drawables:
            rect = d.get_rect()
            surf = d.get_surface()
            self.screen.blit(surf, rect)

            counting_time = pygame.time.get_ticks() - start_time

            # change milliseconds into minutes, seconds, milliseconds
            self.counting_seconds = str( (counting_time%60000)/1000 ).zfill(2)
            self.counting_minutes = str( (counting_time%60000)/60000 ).zfill(2)
            counting_string = "%s:" % (self.counting_minutes) + "%s" % (self.counting_seconds)
            counting_text = font.render(str(counting_string), 1, (51,255,255))
            counting_rect = counting_text.get_rect(center = (56,12))
            self.screen.blit(counting_text, counting_rect)

        pygame.display.update()

class Controller():
    """ All your base are belong to us (this is our controller) """
    def __init__(self,model):
        """ Initialize the controller """
        self.model = model

    def process_events(self):
        """ Process each event so that keys (and the exit button) work """
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and self.model.wc.pos_x > 30:
            self.model.wc.v_x = -speed
            self.model.wc.v_y = 0
        elif keys[K_RIGHT] and self.model.wc.pos_x < 445:
            self.model.wc.v_x = speed
            self.model.wc.v_y = 0
        elif keys[K_UP]and self.model.wc.pos_y > 24:
            self.model.wc.v_x = 0
            self.model.wc.v_y = -speed
        elif keys[K_DOWN] and self.model.wc.pos_y < 351:
            self.model.wc.v_x = 0
            self.model.wc.v_y = speed
        else:
            self.model.wc.v_x = 0
            self.model.wc.v_y = 0

class WCToatfog():
    """ main class because of course """
    def __init__(self):
        """ Initialize """
        self.model = Model(500,400)
        self.view = View(self.model,500,400)
        self.controller = Controller(self.model)

    def run(self):
        """ main runloop """
        frame_count = 0
        last_update_time = time.time()
        while not(self.model.is_dead()):
            self.view.draw()
            self.controller.process_events()
            dt = time.time() - last_update_time
            self.model.update(dt)
            last_update_time = time.time()
        print "You lasted", int(self.view.counting_minutes), "minutes and", int(self.view.counting_seconds), "seconds!"

if __name__ == '__main__':
    """ Setup game """
    game = WCToatfog()
    game.run()