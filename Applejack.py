'''
Created on Apr 19, 2012

@author: Christian
'''

from helpers import *
class Applejack(pygame.sprite.Sprite):
	images = {}
	'''
	classdocs
	'''


	def __init__(self, dpTop):
		pygame.sprite.Sprite.__init__(self)
		self.appleTimer = 1000
		self.dpTop = dpTop
		# load applejack image
		if not Applejack.images:
			Applejack.images['idle'] = pygame.image.load(os.path.join('data', 'images', 'applejack.png'))
			Applejack.images['idle'].convert_alpha()
			Applejack.images['idle'] = pygame.transform.scale(Applejack.images['idle'], (PONY_SIZE, PONY_SIZE))
		
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
		if targets:
			ap = Apple(targets[0], self.dpTop)
			ap.place(self.rect.center)
			self.dpTop.sprites.add(ap)

class Apple(pygame.sprite.Sprite):
	images = {}
	def __init__(self, target, dpTop):
		print "Apple created!"
		pygame.sprite.Sprite.__init__(self)
		
		
		if not Apple.images:
			Apple.images['idle'] = pygame.image.load(os.path.join('data', 'images', 'apple.png'))
			Apple.images['idle'].convert_alpha()
			Apple.images['idle'] = pygame.transform.scale(Apple.images['idle'], (16, 16))
		
		self.image = Apple.images['idle']
		self.rect = self.image.get_rect()
		self.target = target
		self.pos = Vec2d((0,0))
		self.speed = 1000
		self.harm = 10
		self.dpTop = dpTop
		
	def place(self, (x,y)):
		#print "Apple placed at (%d, %d)!" % (x,y)
		self.pos = Vec2d((x,y))
		self.rect.center = self.pos
	
	def update(self, dTime):
		if not self.target.alive():
			self.kill()
		velocity = (self.target.rect.center - self.pos).normalized()*self.speed
		ds = velocity*dTime*1.0/1000
		self.pos += ds
		self.place(self.pos)
		for e in pygame.sprite.spritecollide(self, self.dpTop.enemies, False):
			e.hurt(self.harm)
			self.kill()
			break
