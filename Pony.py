
import pygame

class Pony(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ghost = False
        self.cost = self.__class__.cost
    
    def makeGhost(self):
        self.ghost = True
        
    def makeNotGhost(self):
        self.ghost = False
