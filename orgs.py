# -*- coding: utf-8 -*-
from config import *
import showing as sh
from random import randrange as rndt

import hero
import interaction2 as inter





class Orgs:
    """
    этот класс связан со всем, что связано с оргами
    """
    def __init__(self, name, race, health, force, x, y):
        self.x = x
        self.y = y
        self.health = health
        self.race = race
        self.force = force
        self.color = "red"
        self.rect_id = sh.Entity(x, y, self.color)
        self.mapping = {"s": (0, step), "w": (0, -step),
                        "a": (-step, 0), "d": (step, 0) }


        self.vector = self.mapping["d"]
        self.v_x, self.v_y = self.vector


    def coords(self):

        self.coordinates = self.rect_id.coords()
        self.x1 = self.coordinates[0]
        self.y1 = self.coordinates[1]
        self.x2 = self.coordinates[2]
        self.y2 = self.coordinates[3]

    def checker_collide(self):

        inter.inter.apple(self)
        inter.inter.barrier(self)
        inter.inter.portal(self)
        inter.inter.pillares(self)


    def damage(self, damage):  #урон

        self.health -= damage
        if self.health < 1:
            self.death()

    def death(self):
        sh.canvas.canvas.delete(self.rect_id.rect_id)
        del self

    def move_org(self):

        self.v_x, self.v_y = self.change_direction()
        self.checker_collide()
        sh.canvas.canvas.after(250, self.move_org)

    def change_direction(self):

        if hero.hero.x1 < self.x1:
            return -step,  0

        if hero.hero.y1 < self.y1:
            return 0,  -step

        if hero.hero.x1 > self.x1:
            return step,  0

        if hero.hero.y1 > self.y1:
            return 0,  step


        elif hero.hero.x1 == self.x1 and hero.hero.y1 == self.y1:
            hero.hero.damage(self.force)

        return step, step
