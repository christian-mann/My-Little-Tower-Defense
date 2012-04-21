'''
Created on Apr 19, 2012

@author: Christian
'''

from helpers import *
import copy
images = {}
class Twilight(pygame.sprite.Sprite):
    def __init__(self, dpTop):
        pygame.sprite.Sprite.__init__(self)
        if not images:
            images['idle'] = pygame.image.load(os.path.join('data', 'images', 'twilight.png'))
            images['idle'].convert_alpha()
            images['idle'] = pygame.transform.scale(images['idle'], (PONY_SIZE, PONY_SIZE))
            images['attacking'] = pygame.image.load(os.path.join('data', 'images', 'twilightGlowing.png'))
            images['attacking'].convert_alpha()
            images['attacking'] = pygame.transform.scale(images['attacking'], (PONY_SIZE, PONY_SIZE))
        self.dpTop = dpTop
        
        self.image = images['idle']
        self.rect = self.image.get_rect()
        self.timeTilFire = 1000
        self.range = 500
        self.attacking = False
    
    def place(self, (x,y)):
        self.rect.center = (x,y)
    
    def update(self, dTime):
        self.timeTilFire -= dTime
        if(self.timeTilFire <= 0):
            self.timeTilFire = 1000
            self.toggleAttack()
    
    def toggleAttack(self):
        self.attacking = not self.attacking
        if self.attacking:
            self.image = images['attacking']
        else:
            self.image = images['idle']
    
    def attack(self):
        self.attacking = True
        self.image = images['attacking']