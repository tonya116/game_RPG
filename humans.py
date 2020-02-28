# -*- coding: utf-8 -*-
import showing as sh
from random import randrange as rndt

WIDTH = 640
HEIGHT = 480

class Humans:
    """
    этот класс связан со всем, что связано с героем
    """
    def __init__(self, name, race, health, force, x, y):
        self.x = x
        self.y = y
        self.health = health
        self.race = race
        self.force = force
        self.color = "green"
        self.rect_id = sh.canvas.canvas.create_rectangle(self.x, self.y, self.x + 10, self.y + 10, fill=self.color)

    def coords(self):
        self.coordinates = sh.canvas.canvas.coords(self.rect_id)
        print(self.coordinates)
        sh.canvas.root.after(10,self.coords)

    def check_collide_box(self):

        if int(self.coordinates[0]) < 0:
            sh.canvas.canvas.move(self.rect_id, 10, 0)
        elif int(self.coordinates[1]) < 0:
            sh.canvas.canvas.move(self.rect_id, 0, 10)
        elif int(self.coordinates[2]) > WIDTH:
            sh.canvas.canvas.move(self.rect_id, -10, 0)
        elif int(self.coordinates[3]) > HEIGHT:
            sh.canvas.canvas.move(self.rect_id, 0, -10)

        sh.canvas.root.after(10,self.check_collide_box)


    def damage(self, damage):  #урон
        self.health -= damage

    def move_hero(self):  # движение
        sh.canvas.root.bind('<w>', lambda event: sh.canvas.canvas.move(self.rect_id, 0, -10))
        sh.canvas.root.bind('<s>', lambda event: sh.canvas.canvas.move(self.rect_id, 0, 10))
        sh.canvas.root.bind('<a>', lambda event: sh.canvas.canvas.move(self.rect_id, -10, 0))
        sh.canvas.root.bind('<d>', lambda event: sh.canvas.canvas.move(self.rect_id, 10, 0))


hero = Humans("Den", "Hero", 100, 100, rndt(0, 640, 10),rndt(0, 480, 10))
hero.move_hero()
hero.coords()
hero.check_collide_box()

















    #def regeneration(self):  #регенерация
    #    if self.level_health <= self.health-10:
    #        self.level_magic -= self.level_magic/2
    #        self.level_health += int(0.1 * self.health)
