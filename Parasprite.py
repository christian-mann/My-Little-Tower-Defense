
import pygame
from helpers import *
from Queue import Queue
import random

class Parasprite(pygame.sprite.Sprite):
	images = {}
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.waypoints = []
		
		images = [os.path.join('data', 'images', "parasprite"+str(i)+"-32x32.png") for i in xrange(1,5)]
		images = [pygame.image.load(s) for s in images]
		images = [pygame.transform.scale(i, (32, 32)) for i in images]
		
		self.image = random.choice(images)
		self.rect = self.image.get_rect()
		self.speed = 200
		self.health = 10
		self.harm = 100

		self.pos = Vec2d((0,0))

	
	def place(self,(x,y)):
		self.rect.center = (x,y)
		self.pos = Vec2d((x,y))
	
	def hurt(self, amt):
		self.health -= amt
		if self.health <= 0:
			self.kill()
	
	def update(self, dTime):
		if self.waypoints:
			velocity = (self.waypoints[0] - self.pos).normalized()*self.speed
			ds = velocity*dTime*1.0/1000
			self.pos += ds
			self.place(self.pos)
			if self.rect.collidepoint(self.waypoints[0]):
				del self.waypoints[0]
		else:
			self.kill()