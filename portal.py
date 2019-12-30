# -*- coding: utf-8 -*-
import showing as sh
from random import randrange as rndt

class Portal:
    """
    этот класс связан со всем, что связано с порталами
    """
    def __init__(self, name, race, health, force, x, y):
        self.x = x
        self.y = y
        self.health = health
        self.race = race
        self.force = force
        self.color = "blue"
        self.rect_id = sh.canvas.canvas.create_rectangle(self.x, self.y, self.x + 10, self.y + 10, fill=self.color)

    def coords(self):
        self.coordinates = sh.canvas.canvas.coords(self.rect_id)

p1 = Portal("p1", "portal", 100, 0, rndt(0, 640, 10),rndt(0, 480, 10))
p1.coords()