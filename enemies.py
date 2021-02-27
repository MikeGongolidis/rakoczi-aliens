import pygame
from pygame.sprite import Sprite

class Caterpie(Sprite):

	def __init__(self,settings,screen):

		super(Caterpie,self).__init__()

		self.screen = screen

		self.settings = settings

		self.image = pygame.image.load('assets/cater.png')

		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)


	def update(self):

		self.x += self.settings.caterpie_speed * self.settings.fleet_direction
		self.rect.x = self.x


	def check_edges(self):

		screen_rect = self.screen.get_rect()

		if self.rect.right > screen_rect.right:
			return True
		elif self.rect.left <=0:
			return True




	def blitme(self):

		self.screen.blit(self.image,self.rect)



