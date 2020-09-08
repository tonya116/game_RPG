# -*- coding: utf-8 -*-
from config import *
import showing as sh
from random import randrange as rndt





class Apple:
    """
    этот класс связан со всем, что связано с оргами
    """
    def __init__(self, name, race, force, x, y):
        self.x = x
        self.y = y
        self.race = race
        self.force = force
        self.color = "white"
        self.rect_id = sh.Entity(x, y, self.color)

    def death(self):
        sh.canvas.canvas.delete(self.rect_id.rect_id)
        del self

    def coords(self):
        self.coordinates = self.rect_id.coords()
