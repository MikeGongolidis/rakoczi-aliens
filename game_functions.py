import sys
import pygame

from fire import Fireball


def fire_fireball(settings,screen,dragon,fireballs):

	if len(fireballs) < settings.fireballs_limit:
		new_fireball = Fireball(settings,screen,dragon)
		fireballs.add(new_fireball)		

def check_keydown_events(event,settings,screen,dragon,fireballs):

	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_RIGHT:
			dragon.moving_right = True
		elif event.key == pygame.K_LEFT:
			dragon.moving_left = True

		elif event.key == pygame.K_SPACE:
			fire_fireball(settings,screen,dragon,fireballs)


def check_keyup_events(event,dragon):

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				dragon.moving_right = False
			elif event.key == pygame.K_LEFT:
				dragon.moving_left = False

def check_events(settings,screen,dragon,fireballs):

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		check_keydown_events(event,settings,screen,dragon,fireballs)
		check_keyup_events(event,dragon)


def update_fireballs(fireballs):

	fireballs.update()

	for fireball in fireballs.copy():
		if fireball.rect.bottom < 0 :
			fireballs.remove(fireball)

def update_screen(settings,screen,dragon,fireballs):

	screen.fill(settings.bg_color)
	dragon.blitme()
	for fireball in fireballs:
		fireball.blitme()
	pygame.display.flip()

