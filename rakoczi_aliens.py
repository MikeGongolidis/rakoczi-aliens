import sys
import pygame
from pygame.sprite import Group


import game_functions as gf 
from settings import Settings

from dragon import Dragon 

from enemies import Caterpie

from game_stats import GameStats

from button import Button

from scoreboard import Scoreboard

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def run_game():

	pygame.init()

	game_settings = Settings()


	screen = pygame.display.set_caption("Rakocsi Aliens")

	screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))

	stats = GameStats(game_settings)

	sb = Scoreboard(game_settings,screen,stats)

	play_button = Button(game_settings,screen,"Start")

	dragon = Dragon(game_settings,screen)

	fireballs = Group()

	caterpies = Group()

	gf.create_fleet(game_settings,screen,dragon,caterpies)

	BackGround = Background("assets/background.png", [0,0])


	#INSIDE OF THE GAME LOOP
	while True:

		gf.check_events(game_settings,screen,dragon,caterpies,fireballs,stats,play_button)

		if stats.game_active:

			dragon.update()

			gf.update_caterpies(game_settings,stats,screen,dragon,fireballs,caterpies,sb)
			gf.update_fireballs(game_settings,stats,screen,dragon,fireballs,caterpies,sb)	

		gf.update_screen(game_settings,screen,dragon,caterpies,fireballs,stats,sb,play_button, BackGround)


run_game()
	