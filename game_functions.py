import sys
import pygame
from time import sleep


from fire import Fireball
from enemies import Caterpie




def fire_fireball(settings,screen,dragon,fireballs):

	if len(fireballs) < settings.fireballs_limit:
		new_fireball = Fireball(settings,screen,dragon)
		fireballs.add(new_fireball)		


def dragon_hit(settings,stats,screen,dragon,fireballs,caterpies,sb):

	
	if stats.dragon_lifes > 1:
		stats.dragon_lifes -=1
		sleep(0.5)
	else:
		stats.game_active = False
		stats.reset_stats()
		sb.prep_score() 
		pygame.mouse.set_visible(True)

	caterpies.empty()
	fireballs.empty()

	create_fleet(settings,screen,dragon,caterpies)
	dragon.center_()

	sleep(0.5)

def get_number_caterpies_x(settings,caterpie_width):

	available_space_x = settings.screen_width - 2*caterpie_width
	number_of_caterpies = int(available_space_x / (2*caterpie_width))

	return number_of_caterpies



def get_number_rows(settings,dragon_height,caterpie_height):

	available_space_y = settings.screen_height - (3*caterpie_height) - dragon_height

	number_rows = int(available_space_y / (2*caterpie_height))

	return number_rows



def create_caterpie(settings,screen,caterpies,caterpie_number,row_number):

	caterpie = Caterpie(settings,screen)
	caterpie_width = caterpie.rect.width

	caterpie.x = caterpie_width + 2 * caterpie_width * caterpie_number
	caterpie.rect.y = caterpie.rect.height + 2*caterpie.rect.height*row_number
	caterpie.rect.x = caterpie.x
	caterpies.add(caterpie)


def create_fleet(settings,screen,dragon,caterpies):

	caterpie = Caterpie(settings,screen)

	n_caterpies = get_number_caterpies_x(settings,caterpie.rect.width)
	n_rows = get_number_rows(settings, dragon.rect.height, caterpie.rect.height)

	for row in range(n_rows):

		for caterpie_number in range(n_caterpies):

			create_caterpie(settings,screen,caterpies,caterpie_number,row)




def check_keydown_events(event,settings,screen,dragon,fireballs):

	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_RIGHT:
			dragon.moving_right = True
		elif event.key == pygame.K_LEFT:
			dragon.moving_left = True

		elif event.key == pygame.K_SPACE:
			fire_fireball(settings,screen,dragon,fireballs)
		if event.key == pygame.K_q:
			sys.exit()


def check_keyup_events(event,dragon):

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				dragon.moving_right = False
			elif event.key == pygame.K_LEFT:
				dragon.moving_left = False

def check_play_button(settings,screen,dragon,caterpies,fireballs,stats,play_button,x,y):


	button_clicked = play_button.rect.collidepoint(x,y)
	if not stats.game_active and button_clicked:
		settings.initialize_dynamic_settings()
		pygame.mouse.set_visible(False)
		stats.reset_stats()
		stats.game_active = True

		caterpies.empty()
		fireballs.empty()

		create_fleet(settings,screen,dragon,caterpies)
		dragon.center_()


def check_events(settings,screen,dragon,caterpies,fireballs,stats,play_button):

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y = pygame.mouse.get_pos()
			check_play_button(settings,screen,dragon,caterpies,fireballs,stats,play_button,mouse_x,mouse_y)

		check_keydown_events(event,settings,screen,dragon,fireballs)
		check_keyup_events(event,dragon)

def check_collisions(settings,stats,screen,dragon,fireballs,caterpies,sb):


	collisions = pygame.sprite.groupcollide(fireballs,caterpies,True,True)

	if len(caterpies) == 0:
		stats.score += 1
		sb.prep_score()
		check_high_score(stats,sb)
		fireballs.empty()
		settings.increase_speed()
		create_fleet(settings,screen,dragon,caterpies)



def update_fireballs(settings,stats,screen,dragon,fireballs,caterpies,sb):

	fireballs.update()


	for fireball in fireballs.copy():
		if fireball.rect.bottom < 0 :
			fireballs.remove(fireball)

	check_collisions(settings,stats,screen,dragon,fireballs,caterpies,sb)

def change_fleet_direction(settings,caterpies):

	for caterpie in caterpies.sprites():
		caterpie.rect.y += settings.fleet_drop_speed
	settings.fleet_direction *= -1

def check_fleet_edges(settings,caterpies):

	for caterpie in caterpies.sprites():
		if caterpie.check_edges():
			change_fleet_direction(settings,caterpies)
			break



def update_caterpies(settings,stats,screen,dragon,fireballs,caterpies,sb):
	check_fleet_edges(settings,caterpies)

	caterpies.update()

	if pygame.sprite.spritecollideany(dragon,caterpies):
		dragon_hit(settings,stats,screen,dragon,fireballs,caterpies,sb)

def check_high_score(stats,sb):
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_highscore()


def update_screen(settings,screen,dragon,caterpies,fireballs,stats,sb,button,BackGround):


	#screen.fill(settings.bg_color)
	screen.fill([255, 255, 255])
	screen.blit(BackGround.image, BackGround.rect)
	dragon.blitme()
	caterpies.draw(screen)
	sb.show_score()

	if not stats.game_active:

		button.draw_button()
	for fireball in fireballs:
		fireball.blitme()
	pygame.display.flip()
	

