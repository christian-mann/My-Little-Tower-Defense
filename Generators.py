
import pygame
import os
from helpers import *
from Pinkie import Pinkie
from Rarity import Rarity
from Applejack import Applejack
from Twilight import Twilight
from Rainbowdash import Rainbowdash
from Derpy import Derpy
import numpy

class Generator(pygame.sprite.Sprite):
	allImages = {}
	def __init__(self, imgName, ponyClass, dpTop):
		pygame.sprite.Sprite.__init__(self)
		self.dpTop = dpTop
		if self.__class__.__name__ not in Generator.allImages:
			local = Generator.allImages[self.__class__] = {}
			local['idle'] = load_image(imgName, (64, 64))
			local['inactive'] = self.grayscale(local['idle'])
			local['rollover'] = self.brighten(local['idle'])
	
		self.images = Generator.allImages[self.__class__]
		
		self.image = self.images['idle']
		self.rect = self.image.get_rect()
		self.active = True
		self.hovering = False
		self.ponyClass = ponyClass
		self.locked = False
		
		self.updateImages()
	
	def grayscale(self, img):
		arr = pygame.surfarray.array3d(img)
		#luminosity filter
		avgs = [[(r*0.298 + g*0.587 + b*0.114) for (r,g,b) in col] for col in arr]
		arr = numpy.array([[[avg,avg,avg] for avg in col] for col in avgs])
		return pygame.surfarray.make_surface(arr)
	
	def brighten(self, img):
		arr = pygame.surfarray.array3d(img)
		arr = numpy.array([[map(lambda x: x*1.2 if x*1.2 < 255 else 255, px) for px in col] for col in arr])
		return pygame.surfarray.make_surface(arr)
	
	def hover(self):
		self.hovering = True
		self.updateImages()
		self.dpTop.descField.st = self.ponyClass.description
		self.dpTop.descField.createImage()
		
	def unhover(self):
		self.hovering = False
		self.updateImages()
		self.dpTop.descField.st = " "
		self.dpTop.descField.createImage()
		
	def place(self, (x,y)):
		self.rect.center = (x,y)
		
	def updateImages(self):
		if self.ponyClass.cost > self.dpTop.money or self.locked:
			self.image = self.images['inactive']
		elif self.hovering:
			self.image = self.images['rollover']
		else:
			self.image = self.images['idle']
	
	def update(self, dTime):
		self.updateImages()
			
	def click(self):
		if self.ponyClass.cost <= self.dpTop.money and not self.locked:
			pony = self.ponyClass(self.dpTop)
			pony.makeGhost()
			pony.place(self.rect.center)
			self.dpTop.towerToPlace = pony
			self.dpTop.sprites.add(pony)
	
	def lock(self):
		self.locked = True

	def unlock(self):
		self.locked = False

class PinkiePieGenerator(Generator):
	def __init__(self, dpTop):
		Generator.__init__(self, 'pinkieIcon.png', Pinkie, dpTop)
		
class RarityGenerator(Generator):
	def __init__(self, dpTop):
		Generator.__init__(self, 'rarityIcon.png', Rarity, dpTop)

class ApplejackGenerator(Generator):
	def __init__(self, dpTop):
		Generator.__init__(self, 'applejackIcon.png', Applejack, dpTop)

class TwilightGenerator(Generator):
	def __init__(self, dpTop):
		Generator.__init__(self, 'twilightIcon.png', Twilight, dpTop)

class RainbowdashGenerator(Generator):
	def __init__(self, dpTop):
		Generator.__init__(self, 'rainbowdashIcon.png', Rainbowdash, dpTop)
	
class DerpyGenerator(Generator):
	def __init__(self, dpTop):
		Generator.__init__(self, 'derpyIcon.png', Derpy, dpTop)
