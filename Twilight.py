'''
Created on Apr 19, 2012

@author: Christian
'''

from helpers import *
import copy
from Pony import Pony
class Twilight(Pony):
    images = {}
    cost = 0
    description = "freezes enemies in place. NOT IMPLEMENTED."
    def __init__(self, dpTop):
        Pony.__init__(self)
        if not Twilight.images:
            Twilight.images['idle'] = load_image('twilight.png', (PONY_SIZE, PONY_SIZE))
            Twilight.images['attacking'] = load_image('twilightGlowing.png', (PONY_SIZE, PONY_SIZE))
        self.dpTop = dpTop
        
        self.image = Twilight.images['idle']
        self.rect = self.image.get_rect()
        self.timeTilFire = 1000
        self.range = 500
        self.attacking = False
    
    def place(self, (x,y)):
        self.rect.center = (x,y)
    
    def update(self, dTime):
        self.timeTilFire -= dTime
        if self.timeTilFire <= 0 and not self.ghost:
            self.timeTilFire = 1000
            self.toggleAttack()
    
    def toggleAttack(self):
        self.attacking = not self.attacking
        if self.attacking:
            self.image = Twilight.images['attacking']
        else:
            self.image = Twilight.images['idle']
    
    def attack(self):
        self.attacking = True
        self.image = Twilight.images['attacking']