
class Game:
	def __init__(self):
		self.wins=0
		self.losses=0
	def won(self):
		self.wins+=1
	def lose(self):
		self.losses+=1
	@property	
	def score(self):
		return self.wins-self.losses

g=Game()
g.won()
g.lose()
print (g.wins)
print (g.score)


		
		