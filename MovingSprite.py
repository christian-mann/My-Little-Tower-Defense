
import pygame
from helpers import *

class MovingSprite(pygame.sprite.Sprite):
    def __init__(self, target, speed):
        pygame.sprite.Sprite.__init__(self)
        self.target = target
        self.speed = speed
        self.pos = (0.0, 0.0)
    
    def place(self, (x,y)):
        self.pos = (x*1.0,y*1.0)
        
    def update(self, dt):
        try:
            tar = self.target.rect.center
        except:
            tar = self.target
        if tar is not None:
            distance = Vec2d(tar) - self.rect.center
            velocity = distance.normalized()*1.0*self.speed
            ds = velocity*1.0*dt/1000
            self.pos += ds
            
            self.rect.center = self.pos
            
            if distance.get_length() < ds.get_length()*2:
                self.target = None
