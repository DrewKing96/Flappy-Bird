import pygame
import os
import time
import random

pygame.font.init()

#Defining width and height of game window
WIDTH, HEIGHT = 750, 750

#Establish pygame window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#Define name of game window
pygame.display.set_caption("Flappy Bird")

#Background
BACKGROUND = pygame.image.load(os.path.join("assets", "background.png"))
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

#Bird
BIRD = pygame.image.load(os.path.join("assets", "bird.png"))
BIRD = pygame.transform.scale(BIRD, (100, 100))

class Bird:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.img = BIRD

	def draw(self, window):
		window.blit(self.img, (self.x, self.y))

	def move(self, velocity):
		self.y += velocity


def main():
	run = True
	FPS = 60
	clock = pygame.time.Clock()

	lost = False

	bird_velocity = 2

	bird = Bird(100, 250)

	def redraw_window():
		WIN.blit(BACKGROUND, (0, 0))

		bird.draw(WIN)

		pygame.display.update()

	#Game Loop
	while run:
		clock.tick(FPS)
		redraw_window()
		#bird.move(bird_velocity)

		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			bird.y -= bird_velocity



main()