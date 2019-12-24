## -*- coding: utf-8 -*-
import showing as sh

class SpikePillar:
    """
    этот класс связан со всем, что связано с шипованным столбом в частности
    он наследует класс Entity
    """
    def __init__(self, name, race, health, force, x, y):
        self.x = x
        self.y = y
        self.health = health
        self.race = race
        self.force = force
        self.color = "gray"
        self.rect_id = sh.canvas.canvas.create_rectangle(self.x, self.y, self.x + 10, self.y + 10, fill=self.color)
