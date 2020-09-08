# -*- coding: utf-8 -*-
from config import *
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
        self.color = "orange"
        self.rect_id = sh.Entity(x, y, self.color)


    def coords(self):
        self.coordinates = self.rect_id.coords()


list_of_barriers = []


a = 0
b = 0
for i in map:
    for j in i:

        if a == WIDTH:
            a = 0
            b += step





        if j == "*":
            temp = Barrier("b" + str(3), "barrier", 1, 0, a, b)
            temp.coords()
            list_of_barriers.append(temp)

        a += step





#for barrier in range(count_of_barriers):
#    temp = Barrier("b" + str(barrier), "barrier", 1, 0, rndt(0, WIDTH, step), rndt(0, HEIGHT, step))
#    temp.coords()
#    list_of_barriers.append(temp)
