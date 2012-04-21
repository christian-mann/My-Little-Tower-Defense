'''
Created on Apr 19, 2012

@author: Christian
'''

from helpers import *
from AnimatedSprite import AnimatedSprite
import copy
class Derpy(AnimatedSprite):
	frames = []
	def __init__(self, dpTop):
		self.dpTop = dpTop
		if not Derpy.frames:
			Derpy.frames = [pygame.image.load(os.path.join('data', 'images', 'derpyFlying-'+str(i)+'.png')).convert_alpha() for i in xrange(7)]
			Derpy.frames = map(lambda x: pygame.transform.scale(x, (PONY_SIZE, PONY_SIZE)), Derpy.frames)
		AnimatedSprite.__init__(self, Derpy.frames)

		self.rect = self.image.get_rect()
		self.timeTilFire = 1000
		self.range = 500
		self.attacking = False
	
	def place(self, (x,y)):
		self.rect.center = (x,y)
	
