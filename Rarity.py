'''
Created on Apr 19, 2012

@author: Christian
'''

from helpers import *
from MovingSprite import MovingSprite
from AnimatedSprite import AnimatedSprite
from Pony import Pony
class Rarity(AnimatedSprite, Pony):
    images = {}
    
    cost = 50
    description = "Rarity finds gems! Make sure to click on them to pick them up! Cost: "+str(cost)
    def __init__(self, dpTop):
        Pony.__init__(self)
        if not Rarity.images:
            Rarity.images['idle'] = [load_image('rarityWalking-'+str(i)+'.png', (PONY_SIZE, PONY_SIZE)) for i in xrange(24)]
            Rarity.images['attacking'] = load_image('rarityFindingGems.png', (PONY_SIZE, PONY_SIZE))
        
        self.images = Rarity.images['idle']
        AnimatedSprite.__init__(self, Rarity.images['idle'], 10)
        self.dpTop = dpTop
        self.rect = self.image.get_rect()
        self.timeTilFire = 1000
        self.attackTime = 500
        self.attacking = False
    
    def place(self, (x,y)):
        self.rect.center = (x,y)
        
    def update(self, dTime):
        Pony.update(self)
        if self.attacking:
            self.attackTime -= dTime
            if self.attackTime <= 0:
                # stand back up
                self.attackTime = 500
                self.attacking = False
        else:
            AnimatedSprite.update(self, dTime)
            self.timeTilFire -= dTime
            if self.timeTilFire <= 0 and not self.ghost:
                #find a gem
                self.image = Rarity.images['attacking']
                self.timeTilFire = 3000
                self.attacking = True
                g = Gem(self.dpTop)
                g.place(self.rect.center)
                self.dpTop.sprites.add(g)
                self.dpTop.clickables.add(g)

class Gem(MovingSprite):
    image = None
    RISE_AMOUNT = 50
    SPEED = 300
    def __init__(self, dpTop):
        if not Gem.image:
            Gem.image = load_image('gem.png', (32, 32))
        self.image = Gem.image
        self.rect = self.image.get_rect()
        self.done = False
        self.dpTop = dpTop
        self.pickedUp = False
        self.target = (self.rect.centerx, self.rect.centery - self.RISE_AMOUNT)
        MovingSprite.__init__(self, self.target, self.SPEED)
    
    def place(self, (x,y)):
        MovingSprite.place(self, (x,y))
        self.rect.center = (x,y)
        self.initY = self.rect.centery
        self.target = (self.rect.centerx, self.rect.centery - self.RISE_AMOUNT)
    
    def update(self, dTime):
        MovingSprite.update(self, dTime)
        if self.pickedUp and not self.target:
            print "Killed!"
            self.kill()
    
    def click(self):
        if not self.pickedUp:
            self.speed *= 2
            self.dpTop.getMoney(10)
            self.target = self.dpTop.moneyField
            self.pickedUp = True
