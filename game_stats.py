

class GameStats():

	def __init__(self,settings):

		self.settings = settings
		self.reset_stats()

		self.game_active = False
		self.high_score = 0
		

	def reset_stats(self):

		self.dragon_lifes = self.settings.dragon_lifes

		self.score = 0

