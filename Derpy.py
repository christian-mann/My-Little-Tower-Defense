'''
Created on Apr 19, 2012

@author: Christian
'''

from helpers import *
from AnimatedSprite import AnimatedSprite
from MovingSprite import MovingSprite
from Pony import Pony
class Derpy(AnimatedSprite, MovingSprite, Pony):
	frames = []
	
	cost = 100
	description = "Drops anvils on enemies' heads!"
	def __init__(self, dpTop):
		Pony.__init__(self)
		self.dpTop = dpTop
		if not Derpy.frames:
			Derpy.frames = [load_image('derpyFlying-'+str(i)+'.png', (PONY_SIZE, PONY_SIZE)).convert_alpha() for i in xrange(7)]
		AnimatedSprite.__init__(self, Derpy.frames)

		self.rect = self.image.get_rect()
		
		MovingSprite.__init__(self, None, 1)
		
		self.timeTilFire = 1000
		self.range = 500
		self.attacking = False
		
		self.cooldown = 200
	
	def place(self, (x,y)):
		self.rect.center = (x,y)
	
	def update(self, dTime):
		AnimatedSprite.update(self, dTime)
		if not self.ghost:
			MovingSprite.update(self, dTime)
			if not self.target or not self.target.alive():
				print "finding new target"
				#find a suitable target
				ens = self.dpTop.enemiesWithinRange(self.rect.center, self.range)
				ens.sort(key=lambda x: -x.health)
				if ens:
					self.target = ens[0]
				else:
					self.target = None
			
			self.cooldown -= dTime
			#check whether we can drop an anvil
			if pygame.sprite.spritecollideany(self, self.dpTop.enemies) and self.cooldown <= 0:
				a = Anvil(self.dpTop)
				a.place(self.rect.center)
				self.dpTop.sprites.add(a)
				
				self.cooldown = 200
		
class Anvil(pygame.sprite.Sprite):
	images = {}
	FALLING_TIME = 500
	def __init__(self, dpTop):
		pygame.sprite.Sprite.__init__(self)
		self.dpTop = dpTop
		if not Anvil.images:
			Anvil.images['falling'] = load_image('anvil.png', (64, 64))
		self.image = Anvil.images['falling']
		self.rect = self.image.get_rect()
		
		self.tTime = 0
		self.size = map(lambda x: x*1.0, self.rect.size)
		
	
	def place(self, (x,y)):
		self.rect.center = (x,y) 
	
	def update(self, dTime):
		self.tTime += dTime
		#takes 2 seconds to fall fully, at which point it's 32x32
		if self.tTime <= Anvil.FALLING_TIME:
			oldCen = self.rect.center
			self.size = (64 - (self.tTime*1.0/Anvil.FALLING_TIME)*32, 64 - (self.tTime*1.0/Anvil.FALLING_TIME)*32)
			self.image = pygame.transform.smoothscale(self.image, map(int, self.size))
			self.rect.size = self.size
			self.rect.center = oldCen
		elif self.tTime < Anvil.FALLING_TIME + 200:
			for e in pygame.sprite.spritecollide(self, self.dpTop.enemies, False):
				e.hurt(10)
		elif self.tTime >= Anvil.FALLING_TIME + 200:
			self.kill()