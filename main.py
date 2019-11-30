# encoding: utf-8
import humans
import pygame

pygame.init()
display = pygame.display.set_mode((640,480))
surface = pygame.Surface((640,480))
surface.fill((0,0,0))

hero = humans.Humans(20, "Den", "Human", 100, 1, 1, 1, 1, 100)
all_sprites = pygame.sprite.Group()

all_sprites.add(hero)


done = True
a = 0
while done:
    a += 1
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
            print("GAME OVER")

    print(a)
    hero.update()
    all_sprites.update()

    all_sprites.draw(surface)

    display.blit(surface,(0,0))
    pygame.display.flip()

    pygame.time.delay(1000)
