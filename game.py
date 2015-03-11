
import pygame, sys
import time
from pygame.locals import *
import random
# set up pygame
pygame.init()
# set up the window
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
        self.enemy1 = enemy(width/4, height/4)
        self.enemy2 = enemy(3*width/4, height/4)
        self.enemy3 = enemy(width/4, 3*height/4)
        self.enemy4 = enemy(3*width/4, 3*height/4)

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
        #player_rect = self.get_player().get_drawables()[0]
        #enemy1_rect = self.enemy1.get_drawables()[0]
        if self.wc.pos_x == self.enemy1.pos_x:
            return True
        
        return False

    def update(self, dt):
        """ Updates model and such """
        self.wc.update(dt)
        self.enemy1.update(dt)
        self.enemy2.update(dt)
        self.enemy3.update(dt)
        self.enemy4.update(dt)

class DrawableSurface():

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
     
        # set up the colors
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        DARKBLUE = (0, 0, 83)
        PURPLE = (102, 51, 102)

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
    def __init__(self,pos_x,pos_y):
    
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.v_x = 0
        self.v_y = 0
        self.image = pygame.image.load('images/char1.png')
        self.image.set_colorkey((255,255,255))

    def get_drawables(self):
        return [DrawableSurface(self.image, self.image.get_rect().move(self.pos_x, self.pos_y))]

    def update(self, delta_t):
        self.pos_x += self.v_x*delta_t
        self.pos_y += self.v_y*delta_t

class enemy():
    def __init__(self,pos_x,pos_y):
    
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.v_x = random.randint(50,100)*((2*random.randint(0,1)-1))
        self.v_y = random.randint(50,100)*((2*random.randint(0,1)-1))
        self.image = pygame.image.load('images/enemy.png')
        self.image.set_colorkey((255,255,255))

    def get_drawables(self):
        return [DrawableSurface(self.image, self.image.get_rect().move(self.pos_x, self.pos_y))]

    def update(self, delta_t):
        if self.pos_x < 30 or self.pos_x > 445:
            self.v_x = -1.1*self.v_x
        if self.pos_y < 24 or self.pos_y > 351:
            self.v_y = -1.1*self.v_y
        self.pos_x += self.v_x*delta_t
        self.pos_y += self.v_y*delta_t

    #def up(self):   
    #    self.v_y -= 1

class View():
    def __init__(self, model, width, height):
        """ Initialize view """
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.screen_boundaries = pygame.Rect(0,0,width,height)
        self.model = model

    def draw(self):
        """ Redraw the game window """
        self.screen.fill((0,0,83))
        self.drawables = self.model.get_drawables()
        for d in self.drawables:
            rect = d.get_rect()
            surf = d.get_surface()
            self.screen.blit(surf, rect)
        pygame.display.update()

class Controller():
    def __init__(self,model):
        self.model = model

    # def handle_keyboard event(self, event):
    #     if event.type == KEYDOWN:
    #         print "keydown detected!"
    def process_events(self):
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        #if event.type == MOUSEBUTTONDOWN:
         #   print "mousedown"
            #controller.handle_keyboard_event(event)
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
        #while True:
            self.view.draw()
            self.controller.process_events()
            dt = time.time() - last_update_time
            self.model.update(dt)
            #print dt
            last_update_time = time.time()

if __name__ == '__main__':
    game = WCToatfog()
    game.run()
    # run the game loop
    """
    lead_x = 300
    lead_y = 300
    vx = 0 
    vy = 0
    speed = 10


    while True:
        for event in pygame.event.get():
    #        print event
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
               print "mousedown"
                controller.handle_keyboard_event(event)

            keys = pygame.key.get_pressed()
            if keys[K_a]:
                print "left"
                vx = -speed
                vy = 0
            elif keys[K_d]:
                print "right"
                vx = speed
                vy = 0
            elif keys[K_w]:
                print "up"
                vx = 0
                vy = -speed
            elif keys[K_s]:
                print "down"
                vx = 0
                vy = speed
            else:
                vx = 0
                vy = 0

            if event.type == pygame.KEYDOWN:
                print "keydown detected"
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
                print "keyup detected"
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
        clock.tick(60)
"""