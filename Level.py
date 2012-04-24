
class Level:

	def __init__(self):
		self.title = ''
		self.enemySpeed = ''
		self.waypoints = []
		self.rounds = []

		self.enemyLand = set() #set of rects
		self.startMoney = 0
		self.roundNumber = 0
		
		self.goal = (1.0, 1.0)
		self.backgroundImage = None

		self.introMessage = ""
		self.introMovieName = ""


	
	def inEnemyLand(self, (x,y)):
		return any(r.collidepoint((x,y)) for r in self.enemyLand)

	def currentRound(self):
		return self.rounds[self.roundNumber]

	def inEnemyLandRect(self, r):
		return any(er.contains(r) for er in self.enemyLand)

	def nextRound(self):
		self.roundNumber += 1
		return self.roundNumber < len(self.rounds)

	def noMoreRounds(self):
		return self.roundNumber >= len(self.rounds)
