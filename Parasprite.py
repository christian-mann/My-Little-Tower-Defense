
import pygame
from helpers import *
from Queue import Queue
import random

class Parasprite(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.waypoints = Queue()
		
		fname = "parasprite"+str(random.randint(1,4))+"-32x32.png"
		self.image, self.rect = load_image(fname)
		self.image = self.image.convert_alpha()

		self.speed = 5
		self.health = 10
		self.harm = 100
		
	
	def place(self,(x,y)):
		self.rect.center = (x,y)
	
	def hurt(self, amt):
		self.health -= amt
		if self.health <= 0:
			self.kill()
