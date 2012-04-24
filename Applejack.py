'''
Created on Apr 19, 2012

@author: Christian
'''

from helpers import *
from MovingSprite import MovingSprite
from Pony import Pony
class Applejack(Pony):
	images = {}
	cost = 100
	description = "foobar"


	def __init__(self, dpTop):
		Pony.__init__(self)
		self.appleTimer = 1000
		self.dpTop = dpTop
		# load applejack image
		if not Applejack.images:
			Applejack.images['idle'] = load_image('applejack.png', (PONY_SIZE, PONY_SIZE))
		
		self.image = Applejack.images['idle']
		self.rect = self.image.get_rect()
		self.timeTilFire = 1000
		self.range = 500
	
	def place(self, (x,y)):
		self.rect.center = (x,y)
	
	def update(self, dTime):
		self.timeTilFire -= dTime
		if(self.timeTilFire <= 0):
			self.timeTilFire = 1000
			self.fireApple()
	
	def fireApple(self):
		targets = self.dpTop.enemiesWithinRange(self.rect.center, self.range)
		targets = sorted(targets, key=lambda e: e.health)
		if targets and not self.ghost:
			ap = Apple(targets[0], self.dpTop)
			ap.place(self.rect.center)
			self.dpTop.sprites.add(ap)

class Apple(MovingSprite):
	images = {}
	def __init__(self, target, dpTop):
		print "Apple created!"
		MovingSprite.__init__(self, target, 1000)
		if not Apple.images:
			Apple.images['idle'] = pygame.image.load(os.path.join('data', 'images', 'apple.png'))
			Apple.images['idle'].convert_alpha()
			Apple.images['idle'] = pygame.transform.scale(Apple.images['idle'], (16, 16))
		
		self.image = Apple.images['idle']
		self.rect = self.image.get_rect()
		self.target = target
		
		self.pos = Vec2d((0,0))
		self.harm = 10
		self.dpTop = dpTop
		
	def place(self, (x,y)):
		#print "Apple placed at (%d, %d)!" % (x,y)
		self.pos = Vec2d((x,y))
		self.rect.center = self.pos
	
	def update(self, dTime):
		MovingSprite.update(self, dTime)
		if self.target and not self.target.alive():
			self.kill()
		for e in pygame.sprite.spritecollide(self, self.dpTop.enemies, False):
			e.hurt(self.harm)
			self.kill()
			break
