
import pygame
import os

class VolumeControl(pygame.sprite.Sprite):
	images = []
	def __init__(self, music):
		pygame.sprite.Sprite.__init__(self)

		self.images = [(s, pygame.image.load(os.path.join('data', 'images', 'volume-'+s+'.png')).convert_alpha()) for s in ['muted', 'low', 'medium', 'high']]
		self.images = [(s,pygame.transform.scale(i, (32, 32))) for (s,i) in self.images]
		self.images = dict(self.images)

		self.music = music

		#set initial image
		self.image = self.images[self.corrImage(self.music.get_volume())]
		self.rect = self.image.get_rect()
	
	def corrImage(self, val):
		if val <= 0.00001:
			return 'muted'
		elif val <= 0.33:
			return 'low'
		elif val <= 0.67:
			return 'medium'
		else:
			return 'high'
	
	def update(self, dTime):
		self.image = self.images[self.corrImage(self.music.get_volume())]
	
	def place(self, (x,y)):
		self.rect.center = (x,y)
	
	def click(self):
		vol = self.music.get_volume()
		if vol <= 0.0001:
			vol = 0.3
		elif vol <= 0.33:
			vol = 0.6
		elif vol <= 0.67:
			vol = 0.99
		else:
			vol = 0
		self.music.set_volume(vol)
