
from helpers import *
import pygame

class Goal(pygame.sprite.Sprite):
    def __init__(self, health, size):
        self.maxHealth = self.health = health
        self.width = size.x
        self.height = size.y
        
        self.image = load_image("library.png", (128, 128))
        self.rect = self.image.get_rect()
    
    def place(self, (x,y)):
        self.x, self.y = x*1.0, y*1.0
    
    def door(self):
        return (self.rect.x + self.rect.width/2, self.rect.y + self.rect.height/2)