# encoding: utf-8
# encoding: utf-8
# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import humans
import random

WIDTH = 800
HEIGHT = 650
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
hero = humans.Humans(20, "Den", "Human", 100, 1, 1, 1, 1, 100)
all_sprites.add(hero)

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False


    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            hero.rect.y -= 10
            pygame.time.delay(50)
        if event.key == pygame.K_s:
            hero.rect.y += 10
            pygame.time.delay(50)
        if event.key == pygame.K_a:
            hero.rect.x -= 10
            pygame.time.delay(50)
        if event.key == pygame.K_d:
            hero.rect.x += 10
            pygame.time.delay(50)

    # Обновление
    all_sprites.update()

    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
