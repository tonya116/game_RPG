## -*- coding: utf-8 -*-

import showing as sh

class Humans:
    """
    этот класс связан со всем, что связано с героем в частности

    """
    def __init__(self, name, race, health, force, x, y):
        self.x = x
        self.y = y
        self.health = health
        self.race = race
        self.force = force
        self.color = "green"
        self.rect_id = sh.obj.canvas.create_rectangle(self.x, self.y, self.x + 10, self.y + 10, fill=self.color)

    def damage(self, damage):  #урон
        self.health -= damage

    def move_hero(self):  # движение
        sh.obj.root.bind('<w>', lambda event: sh.obj.canvas.move(self.rect_id, 0, -10))
        sh.obj.root.bind('<s>', lambda event: sh.obj.canvas.move(self.rect_id, 0, 10))
        sh.obj.root.bind('<a>', lambda event: sh.obj.canvas.move(self.rect_id, -10, 0))
        sh.obj.root.bind('<d>', lambda event: sh.obj.canvas.move(self.rect_id, 10, 0))




















    #def regeneration(self):  #регенерация
    #    if self.level_health <= self.health-10:
    #        self.level_magic -= self.level_magic/2
    #        self.level_health += int(0.1 * self.health)
