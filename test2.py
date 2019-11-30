# encoding: utf-8

import pygame
pygame.init()

display = pygame.display.set_mode((400, 400))



hero = pygame.Surface((100, 100))
hero.fill((255, 0, 0))
x = 0
y = 50

# порядок прорисовки важен!
display.blit(hero, (x, y))


pygame.display.update()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()



    display.fill((0, 0, 0))
    display.blit(hero, (x, y))
    pygame.display.update()
    pygame.time.delay(30)
