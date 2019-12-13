## -*- coding: utf-8 -*-
import entity as sh

class SpikePillar(sh.Entity):
    """
    этот класс связан со всем, что связано с шипованным столбом в частности
    он наследует класс Entity
    """
    def __init__(self, name, race, health, force):
        sh.Entity.__init__(self, name, race, health, force, x, y)
        self.health = health
        self.x = x
        self.y = y
