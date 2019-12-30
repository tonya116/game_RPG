# -*- coding: utf-8 -*-
import showing as sh

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


    def damage(self, damage):  #урон
        self.health -= damage

    def move_hero(self):  # движение
        sh.canvas.root.bind('<w>', lambda event: sh.canvas.canvas.move(self.rect_id, 0, -10))
        sh.canvas.root.bind('<s>', lambda event: sh.canvas.canvas.move(self.rect_id, 0, 10))
        sh.canvas.root.bind('<a>', lambda event: sh.canvas.canvas.move(self.rect_id, -10, 0))
        sh.canvas.root.bind('<d>', lambda event: sh.canvas.canvas.move(self.rect_id, 10, 0))



hero = Humans("Den", "Hero", 100, 100, 150, 200)
hero.move_hero()
hero.coords()

















    #def regeneration(self):  #регенерация
    #    if self.level_health <= self.health-10:
    #        self.level_magic -= self.level_magic/2
    #        self.level_health += int(0.1 * self.health)
