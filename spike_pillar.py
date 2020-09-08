# -*- coding: utf-8 -*-

from config import *
import showing as sh
from random import randrange as rndt

class SpikePillar:
    """
    этот класс связан со всем, что связано с шипованным столбом
    """
    def __init__(self, name, race, health, force, x, y):
        self.x = x
        self.y = y
        self.health = health
        self.race = race
        self.force = force
        self.color = "brown"
        self.rect_id = sh.Entity(x, y, self.color)

    def coords(self):
        self.coordinates = self.rect_id.coords()

    def death(self):
        sh.canvas.canvas.delete(self.rect_id.rect_id)
        del self
