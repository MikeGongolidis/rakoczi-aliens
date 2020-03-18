

class GameStats():

	def __init__(self,settings):

		self.settings = settings
		self.reset_stats()

		self.game_active = True

	def reset_stats(self):

		self.dragon_lifes = self.settings.dragon_lifes