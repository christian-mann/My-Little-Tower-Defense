
import pygame

from DefenseMain import DefenseMain
from Applejack import Applejack
from Twilight import Twilight
from Rainbowdash import Rainbowdash
from Derpy import Derpy
from Rarity import Rarity
from Parasprite import Parasprite
from helpers import *

dp = DefenseMain()


def playGame():
	pygame.key.set_repeat(30, 30)
	
	dp.setBackground('backgroundImage.png')
	dp.initializeStatic()

	#intro movie
	dp.showMovie('applejackIntro-lowRes.mpg')
	dp.playMusic('applejackTheme.mp3')

	dp.showMessage("Welcome to Equestria!\n Defend the castle against the parasprites.\n Click on Applejack's icon in the top-right,\n then place her on the screen.\n    (Click this scroll to dismiss it)")
	dp.lockAll()
	dp.unlock(Applejack)

	for i in xrange(5):
		p = Parasprite(dp)
		p.place((-0.1*dp.pWidth*i, 0.1*dp.pHeight))
		dp.addEnemy(p)
	
	prevHealth = dp.health
	while True:
		dp.updateRender()
		if 0 < dp.health <= 15 and not 0 < prevHealth <= 15:
			dp.playMusic('thisIsBad.wav', False)

		prevHealth = dp.health
		if dp.gameOver:
			return
		elif all(not e.alive() for e in dp.enemies):
			break

while True:
	dp.playMusic(os.path.join('mainTheme.mp3'), True)
	option = dp.mainMenu()
	if option == "Play Game":
		playGame()
		if dp.gameOver:
			dp.playMusic(None)
			dp.playMusic('nooooooooooooo.wav', bg=False)
			dp.showMessage("I'm recommending you for remedial study.\n   -Celestia")
		else:
			dp.playMusic(None)
			dp.playMusic('yesyesyes.mp3', bg=False)
			dp.showMessage('Well done.')
	elif option == "Instructions":
		dp.showPonies()
	elif option == "Credits":
		dp.showCredits()
	elif option == "Quit":
		dp.quitGame()
