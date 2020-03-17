import pygame
from pygame.sprite import Sprite


class Fireball(Sprite):

	def __init__(self,settings,screen,dragon):

		super(Fireball,self).__init__()
		self.screen = screen

		self.image = pygame.image.load('fireball.png')

		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		#self.rect = pygame.Rect(0,0,settings.bullet_width,settings.bullet_height)

		self.rect.centerx = dragon.rect.centerx
		self.rect.top = dragon.rect.top

		self.y = float(self.rect.y)

		self.speed_factor = settings.fireball_speed_factor

	def update(self):

		self.y -= self.speed_factor

		self.rect.y = self.y

	def blitme(self):

		self.screen.blit(self.image,self.rect)
