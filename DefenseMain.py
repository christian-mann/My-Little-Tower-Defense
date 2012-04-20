#!/usr/bin/env python
from Applejack import Applejack
from Parasprite import Parasprite
from helpers import *
from pygame.locals import *
import os
import pygame
import random
import sys
import menu

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

Main = 0
class DefenseMain:
	
	def __init__(self, width=1024,height=768):
		"""Initialize"""
		"""Initialize PyGame"""
		pygame.init()
		"""Set the window Size"""
		self.fWidth = width
		self.fHeight = height
		"""Create the Screen"""
		self.screen = pygame.display.set_mode((self.fWidth, self.fHeight))
		self.sprites = pygame.sprite.RenderUpdates()
		self.towers = pygame.sprite.Group()
		self.enemies = pygame.sprite.Group()
		self.message = ""
	
	def MainLoop(self):
		pygame.mixer.music.load(os.path.join('data', 'audio', 'background.mp3'))
		pygame.mixer.music.play()
		
		option = menu.Menu.blockMenu(["Play", "Meet the Ponies", "Enemies", "Quit"], self.screen)
		
		pygame.mixer.music.fadeout(1000)
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
		print "loading background"
		self.background = pygame.image.load(os.path.join('data', 'images', 'backgroundImage.png'))
		self.background = pygame.transform.scale(self.background, (self.fWidth, self.fHeight))
		#self.background = pygame.Surface(self.screen.get_size())
		
		clock = pygame.time.Clock()
		while True:
			dTime = clock.tick(100)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == MOUSEBUTTONDOWN:
					if event.button == 1:
						# create new AppleJack
						aj = Applejack(self)
						aj.place(event.pos)
						if not pygame.sprite.spritecollideany(aj, self.sprites):
							self.sprites.add(aj)
							self.towers.add(aj)
							self.showMessage("Applejack tower created!")
					elif event.button == 3:
						# create new Parasprite
						p = Parasprite()
						p.place(event.pos)
						self.sprites.add(p)
						self.enemies.add(p)
				elif event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						self.quitGame()
			"""update all the things"""
			for s in self.sprites:
				s.update(dTime)
				
			"""draw all text"""
			self.screen.blit(self.background, (0,0))
			if pygame.font:
				font = pygame.font.Font(None, 36)
				text = font.render("Pony TD", 1, (255, 45, 68))
				textpos = text.get_rect(centerx=self.background.get_width()/2)
				self.screen.blit(text, textpos)
				
				text = font.render("Average FPS: "+("%2.2f" % (1000/dTime)), 1, (100, 0, 0))
				textpos = text.get_rect(x=0, y=0)
				self.screen.blit(text, textpos)
				
				if self.message:
					font = pygame.font.Font(None, 18)
					text = font.render(self.message, 1, (0, 0, 0))
					textpos = text.get_rect(x=0, y=0)
					self.screen.fill((255, 255, 255), textpos)
					self.screen.blit(text, textpos)
			
			self.sprites.draw(self.screen)
			pygame.display.flip()
	
	def quitGame(self):
		pygame.quit()
		sys.exit(0)
	
	def showMessage(self, msg):
		self.message = msg

if __name__ == "__main__":
	Main = DefenseMain()
	Main.MainLoop()
