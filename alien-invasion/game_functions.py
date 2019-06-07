import sys
import pygame

from bullet import Bullet

def check_events(ai_settings, screen,
	ship, bullets):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				check_keydown_events(event, ai_settings, screen,
					ship, bullets)

			elif event.type == pygame.KEYUP:
				check_keyup_events(event, ship)


				
def check_keydown_events(event, ai_settings, screen,
	ship, bullets):
	"""respond to keypresses"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		# create a new bullet and add it to the bullets group
		new_bullet = Bullet(ai_settings, screen,
			ship)
		bullets.add(new_bullet)

def check_keyup_events(event, ship):
	"""respond to keyreleases"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False				
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False


def update_screen(ai_settings, screen, ship, bullets):
	"""Update images on the screen and flip to a new screen."""
	screen.fill(ai_settings.bg_color)

	# redraw all bullets behind ship and aliens
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	ship.blitme()
	# make most recently drawn screen visible
	pygame.display.flip()
