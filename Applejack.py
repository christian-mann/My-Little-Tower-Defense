'''
Created on Apr 19, 2012

@author: Christian
'''

from helpers import *
image = 0
class Applejack(pygame.sprite.Sprite):
	'''
	classdocs
	'''


	def __init__(self, dpTop):
		pygame.sprite.Sprite.__init__(self)
		self.x_dist = 5
		self.y_dist = 5
		self.appleTimer = 1000
		self.dpTop = dpTop
		# load applejack image
		self.image, self.rect = load_image('applejack-64x64.png', -1)
		#self.image = pygame.transform.scale(self.image, (64, 64))
		#self.rect.size = (64, 64)
		self.timeTilFire = 1000
		
		self.RANGE = 1000
	
	def place(self, (x,y)):
		self.rect.center = (x,y)
	
	def update(self, dTime):
		self.timeTilFire -= dTime
		if(self.timeTilFire <= 0):
			self.timeTilFire = 1000
			self.fireApple()
	
	def fireApple(self):
		targets = [e for e in self.dpTop.enemies if (Vec2d(e.rect.center) - Vec2d(self.rect.center)).get_length() < self.RANGE]
		targets = sorted(targets, key=lambda e: e.health)
		if targets:
			ap = Apple(targets[0], self.dpTop)
			ap.place(self.rect.center)
			self.dpTop.sprites.add(ap)

class Apple(pygame.sprite.Sprite):
	def __init__(self, target, dpTop):
		print "Apple created!"
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image('apple.png')
		self.image.convert_alpha()
		self.image = pygame.transform.scale(self.image, (16, 16))
		self.rect.size = (16, 16)
		self.target = target
		self.pos = Vec2d((0,0))
		self.SPEED = 1000
		self.HARM = 10
		self.dpTop = dpTop
		
	def place(self, (x,y)):
		#print "Apple placed at (%d, %d)!" % (x,y)
		self.pos = Vec2d((x,y))
		self.rect.center = self.pos
	
	def update(self, dTime):
		if not self.target.alive():
			self.kill()
		velocity = (self.target.rect.center - self.pos).normalized()*self.SPEED
		ds = velocity*dTime*1.0/1000
		self.pos += ds
		self.place(self.pos)
		for e in pygame.sprite.spritecollide(self, self.dpTop.enemies, False):
			e.hurt(self.HARM)
			self.kill()
			break
