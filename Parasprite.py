
import pygame
from helpers import *
from MovingSprite import MovingSprite
import random

class Parasprite(MovingSprite):
	images = [os.path.join('data', 'images', "parasprite"+str(i)+".png") for i in xrange(1,5)]
	images = [pygame.image.load(s) for s in images]
	images = [pygame.transform.scale(i, (32, 32)) for i in images]
	def __init__(self, dpTop):
		MovingSprite.__init__(self, None, 200)
		self.waypoints = dpTop.enemyPath[:]
		
		self.image = random.choice(Parasprite.images)
		
		self.rect = self.image.get_rect()
		self.speed = 200
		self.health = 10
		self.harm = 19
		
		self.dpTop = dpTop

		self.pos = Vec2d((0,0))

	
	def place(self,(x,y)):
		self.rect.center = (x,y)
		self.pos = Vec2d((x,y))
	
	def hurt(self, amt):
		self.health -= amt
		if self.health <= 0:
			self.kill()
	
	def update(self, dTime):
		MovingSprite.update(self, dTime)
		if not self.target:
			if self.waypoints:
				self.target = self.waypoints[0]
				del self.waypoints[0]
			else:
                                self.dpTop.health -= self.harm
                                self.dpTop.healthField.st = "Health: " + str(self.dpTop.health)
                                self.dpTop.healthField.createImage()
				self.kill()
