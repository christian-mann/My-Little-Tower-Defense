'''
Created on Apr 19, 2012

@author: Christian
'''

from helpers import *
from Pony import Pony
class Pinkie(Pony):
    images = {}
    sounds = {}
    
    cost = 100
    description = "Pinkie Pie with a Party Cannon!"
    def __init__(self, dpTop):
        Pony.__init__(self)
        if not Pinkie.images:
            Pinkie.images['idle'] = pygame.transform.flip(load_image('pinkieCannonIdle.png', (PONY_SIZE, PONY_SIZE)), True, False)
            Pinkie.images['attacking'] = pygame.transform.flip(load_image('pinkieCannonFiring.png', (PONY_SIZE, PONY_SIZE)), True, False)
        if not Pinkie.sounds:
            Pinkie.sounds['attack'] = pygame.mixer.Sound(os.path.join('data', 'audio', 'partyCannon.wav'))
            
        self.dpTop = dpTop
        
        self.image = Pinkie.images['idle']
        self.rect = self.image.get_rect()
        self.timeTilFire = 1000
        self.attackTime = 500
        self.range = 500
        self.attacking = False
    
    def place(self, (x,y)):
        self.rect.center = (x,y)
    
    def update(self, dTime):
        if self.attacking:
            self.attackTime -= dTime
            if self.attackTime <= 0:
                self.toggleAttack()
                self.attackTime = 500
        else:
            self.timeTilFire -= dTime
            if(self.timeTilFire <= 0):
                targets = self.dpTop.enemiesWithinRange(self.rect.center, self.range)
                targets.sort(key=lambda x: x.health)
                if targets:
                    print targets[0].rect
                    e = Explosion(self.dpTop)
                    e.place(targets[0].rect.center)
                    self.dpTop.sprites.add(e)
                    self.toggleAttack()
                    self.timeTilFire = 3000
    
    def toggleAttack(self):
        self.attacking = not self.attacking
        if self.attacking:
            self.image = Pinkie.images['attacking']
            self.sounds['attack'].play()
            print "played!"
        else:
            self.image = Pinkie.images['idle']

class Explosion(pygame.sprite.Sprite):
    images = {}
    def __init__(self, dpTop):
        pygame.sprite.Sprite.__init__(self)
        if not Explosion.images:
            Explosion.images['idle'] = load_image('explosion.png', (32, 32))
        
        self.image = Explosion.images['idle']
        self.rect = self.image.get_rect()
        self.dpTop = dpTop
        self.lifetime = 500
        
    def update(self, dTime):
        self.lifetime -= dTime
        if self.lifetime <= 0:
            self.kill()
            
    def place(self, (x,y)):
        self.rect.center = (x,y)
        for e in pygame.sprite.spritecollide(self, self.dpTop.enemies, False):
            e.hurt(10)