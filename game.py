
import pygame, sys
import time
from pygame.locals import *
# set up pygame
pygame.init()
# set up the window
speed = 10


class Model():
    """ Our model """
    def __init__(self,width,height):
        """ Initialize"""
        self.width = width
        self.height = height
        self.wc = WC(width/2, height/2)
        self.background = Background(width, height)
        self.obstacles = []

    def get_drawables(self):
        """ Return a list of DrawableSurfaces for the model """
        drawables = self.background.get_drawables()+self.wc.get_drawables()
        for obstacle in self.obstacles:
            drawables += obstacle.get_drawables()
        return drawables

    def get_player(self):
        """ returns the amazing W.C. Toatfog """
        return self.wc

    def update(self, dt):
        """ Updates model and such """
        self.wc.update(dt)

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

    def get_drawables(self):
        """ get the drawables """
        drawables = []
        return drawables + self.get_ground_drawables()

    def get_ground_drawables(self):
        """ get the drawables that are the ground and everything on it """
        drawables = []
        
        # set up the colors
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        DARKBLUE = (0, 0, 83)
        PURPLE = (102, 51, 102)
        
        r = [pygame.Rect(0, 0, 500, 20), pygame.Rect(0, 0, 20, 180), pygame.Rect(0, 220, 20, 180), 
                        pygame.Rect(480, 0, 20, 180), pygame.Rect(480, 220, 20, 180), pygame.Rect(0, 380, 500, 20)]
        for rect in r:
            drawables.append(DrawableSurface(PURPLE,rect))
        return drawables


class WC():
    def __init__(self,pos_x,pos_y):
    
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.v_x = 0
        self.v_y = 0
        # TODO: don't depend on relative path
        self.image = pygame.image.load('images/char1.png')
        self.image.set_colorkey((255,255,255))

    def get_drawables(self):
        return [DrawableSurface(self.image, self.image.get_rect().move(self.pos_x, self.pos_y))]

    def update(self, delta_t):
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
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #if event.type == MOUSEBUTTONDOWN:
         #   print "mousedown"
            #controller.handle_keyboard_event(event)
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            #print "left"
            self.model.wc.v_x = -speed
            self.model.wc.v_y = 0
        elif keys[K_d]:
            #print "right"
            self.model.wc.v_x = speed
            self.model.wc.v_y = 0
        elif keys[K_w]:
            #print "up"
            self.model.wc.v_x = 0
            self.model.wc.v_y = -speed
        elif keys[K_s]:
            #print "down"
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
        while True:
            self.view.draw()
            self.controller.process_events()
            dt = time.time() - last_update_time
            self.model.update(dt)
            print dt
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