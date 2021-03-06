# -*- coding: utf-8 -*-
from config import *
from random import randrange as rndt

import showing as sh



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

        self.rect_id = sh.Entity(x, y, self.color)

    def death(self):
        sh.canvas.canvas.delete(self.rect_id.rect_id)
        del self


    def coords(self):
        self.coordinates = self.rect_id.coords()
