# -*- coding: utf-8 -*-
import showing as sh
from random import randrange as rndt



class Barrier:
    """
    этот класс связан со всем, что связано с преградами
    """
    def __init__(self, name, race, health, force, x, y):
        self.x = x
        self.y = y
        self.health = health
        self.race = race
        self.force = force
        self.color = "yellow"
        self.rect_id = sh.canvas.canvas.create_rectangle(self.x, self.y, self.x + 10, self.y + 10, fill=self.color)

    def coords(self):
        self.coordinates = sh.canvas.canvas.coords(self.rect_id)


list_of_barriers = []
count_of_barriers = 300

for barrier in range(count_of_barriers):
    temp = Barrier("b" + str(barrier), "barrier", 1, 0, rndt(0, 640, 10), rndt(0, 480, 10))
    temp.coords()
    list_of_barriers.append(temp)
