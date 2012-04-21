#!/usr/bin/env python
from Applejack import Applejack
from Parasprite import Parasprite
from Rainbowdash import Rainbowdash
from Derpy import Derpy
from Twilight import Twilight
from VolumeControl import VolumeControl
from helpers import *
from pygame.locals import *
import os
import pygame
import random
import sys
import menu
import time

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

Main = 0
class DefenseMain:
	
	def __init__(self, width=1024,height=768):
		pygame.init()
		self.fWidth = width
		self.fHeight = height
		self.screen = pygame.display.set_mode((self.fWidth, self.fHeight))
		self.sprites = pygame.sprite.RenderUpdates()
		self.towers = pygame.sprite.Group()
		self.clickables = pygame.sprite.Group()
		self.hoverables = pygame.sprite.Group()
		self.enemies = pygame.sprite.Group()
		self.message = ""
		
		self.enemyPath = [(0.00, 0.00), (0.35, 0.11), (0.37, 0.25), (0.14, 0.45), (0.16, 0.62), (0.28, 0.72), (0.48, 0.70), (0.51, 0.58), (0.47, 0.40), (0.65, 0.11), (0.81, 0.13), (0.78, 0.37), (0.80, 0.68), (0.90, 0.78), (1, 0.78)]
		self.enemyPath = [(x*width,y*height) for (x,y) in self.enemyPath]
	
	def main(self):
		pygame.mixer.init()
		pygame.mixer.music.load(os.path.join('data', 'audio', 'background.mp3'))
		pygame.mixer.music.play()
		
		while True:
			#option = menu.Menu.blockMenu(["Play", "Meet the Ponies", "Enemies", "Quit"], self.screen)
			option = 0
			
			#pygame.mixer.music.fadeout(1000)
			pygame.mixer.music.load(os.path.join('data', 'audio', 'level1.mp3'))
			pygame.mixer.music.play()
			if option == 0:
				self.playGame()
			elif option == 1:
				self.showPonies()
			elif option == 2:
				self.showEnemies()
			elif option == 3:
				self.quitGame()
			
	
	def LoadSprites(self):
		global fWidth, fHeight
	
		
	def playGame(self):
		self.LoadSprites()
		pygame.key.set_repeat(30,30)
		self.background = pygame.image.load(os.path.join('data', 'images', 'backgroundImage.png'))
		self.background = pygame.transform.scale(self.background, (self.fWidth, self.fHeight))
		self.screen.blit(self.background, (0,0))
		
		pygame.mixer.music.set_volume(0)
		self.volControl = VolumeControl(pygame.mixer.music)
		self.volControl.rect.topright = (self.fWidth, 0)
		self.clickables.add(self.volControl)
		self.sprites.add(self.volControl)
		clock = pygame.time.Clock()
		while True:
			dTime = clock.tick(100)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == MOUSEBUTTONDOWN:
					for s in self.clickables:
						if s.rect.collidepoint(event.pos):
							s.click()
				elif event.type == MOUSEMOTION:
					for s in self.hoverables:
						if s.rect.collidepoint(event.pos):
							s.hover()
							#todo notify unhover
				elif event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						self.quitGame()
			"""update all the things"""
			self.sprites.update(dTime)
			self.sprites.clear(self.screen, self.background)
			changes = self.sprites.draw(self.screen)
			pygame.display.update(changes)
			pygame.display.flip()
	
	def quitGame(self):
		pygame.quit()
		sys.exit(0)
	
	def showMessage(self, msg):
		self.message = msg
	
	def enemiesWithinRange(self, pt, r):
		targets = [e for e in self.dpTop.enemies if (Vec2d(pt) - Vec2d(e.rect.center)).get_length() < r]
		return targets

	def showPonies(self):
		ponyImg = pygame.image.load(os.path.join('data', 'images', 'ponyImg.png'))
		ponyImg = pygame.transform.scale(ponyImg, (self.fWidth, self.fHeight))
		while True:
			for event in pygame.event.get():
				if event.type == KEYDOWN and event.key == K_ESCAPE:
					quit()
				if event.type in [MOUSEBUTTONDOWN, KEYDOWN]:
					return
				if event.type == QUIT:
					self.quitGame()
			self.screen.blit(ponyImg, (0,0))
			pygame.display.flip()

if __name__ == "__main__":
	Main = DefenseMain()
	Main.main()
