'''
Created on Apr 19, 2012

@author: Christian
'''

from helpers import *
from Pony import Pony
class Rainbowdash(Pony):
	images = {}
	cost = 100
	description = "Foobar"
	def __init__(self, dpTop):
		Pony.__init__(self)
		self.dpTop = dpTop
		# load rainbowdash image
		if not Rainbowdash.images:
			Rainbowdash.images['idle'] = load_image('rainbowdash.png', (PONY_SIZE, PONY_SIZE))
		
		self.image = Rainbowdash.images['idle']
		self.rect = self.image.get_rect()
		self.timeTilFire = 1000
		self.range = 500
		self.attacking = False
	
	def place(self, (x,y)):
		self.rect.center = (x,y)
	
	def update(self, dTime):
		self.timeTilFire -= dTime
		if self.timeTilFire <= 0 and not self.ghost:
			self.timeTilFire = 1000
			self.attack()
	
	def attack(self):
		mrd = MovingRainbowdash(self.dpTop)
		mrd.setTarget((self.rect.center[0], self.rect.center[1] - 300))
		mrd.place(self.rect.center)
		mrd.go()
		self.dpTop.sprites.add(mrd)


class MovingRainbowdash(Rainbowdash):
	def __init__(self, dpTop):
		Rainbowdash.__init__(self, dpTop)
		
		self.pos = Vec2d(0.0,0.0)
		self.maxKills = float('inf')
		self.going = False
		self.speed = 1000
	
	def setTarget(self, (x,y)):
		self.target = Vec2d(x,y)
	
	def place(self, (x,y)):
		self.pos = Vec2d(x,y)
		self.rect.center = self.pos
		
	def setMaxKills(self, n):
		self.maxKills = n
	
	def go(self):
		self.going = True
	
	
	def update(self, dTime):
		if self.going:
			velocity = (self.target - self.rect.center).normalized()*self.speed
			ds = velocity * (dTime*1.0/1000)
			self.pos += ds
			self.place(self.pos)
			#make contrails
			for i in xrange(int(ds.get_length()/5) - 1):
				offset = i*5
				trail = RainbowTrail(200)
				trail.rect.midbottom = (self.rect.midbottom + Vec2d(0, offset))
				self.dpTop.sprites.add(trail)
			for e in pygame.sprite.spritecollide(self, self.dpTop.enemies, False):
				e.hurt(10)
				self.maxKills -= 1
				if self.maxKills == 0:
					self.kill()
					break
			if self.rect.collidepoint(self.target):
				self.kill()

class RainbowTrail(pygame.sprite.Sprite):
	def __init__(self, timeout):
		pygame.sprite.Sprite.__init__(self)
		self.pos = Vec2d(0.0,0.0)
		self.timeout = timeout
		self.image = load_image('rainbowGradient.png')
		self.rect = self.image.get_rect()
	
	def update(self, dTime):
		self.timeout -= dTime
		if self.timeout < 0:
			self.kill()
	
	def place(self, (x,y)):
		self.pos = Vec2d(x,y)
		self.rect.center = self.pos
