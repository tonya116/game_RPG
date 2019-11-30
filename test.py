# encoding: utf-8
import pygame

pygame.init()
window = pygame.display.set_mode((640,480))
pygame.display.init()
screen = pygame.Surface((640,480))

done = True

while done:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			done = False
			print("GAME OVER")

	screen.fill((0,0,0))
	sprite_group.draw(screen)
	window.blit(screen,(0,0))
	pygame.display.flip()
	pygame.time.delay(5)
