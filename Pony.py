
import pygame

class Pony(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ghost = False
        self.cost = 100
    
    def makeGhost(self):
        self.ghost = True
        
    def makeNotGhost(self):
        self.ghost = False