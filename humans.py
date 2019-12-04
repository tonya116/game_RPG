## -*- coding: utf-8 -*-
from showing import *


class Humans(Entity):
    """
    этот класс связан со всем, что связано с героем в частности
    он наследует класс Entity
    """
    def __init__(self, age, name, race, health, force, stamina, iq, magic, money):
        Entity.__init__(self, age, name, race, health, force, stamina, iq, magic, money)
        self.stamina = stamina
        self.iq = iq
        self.magic = magic
        self.level_health = self.health
        self.level_force = 100
        self.level_stamina = 100
        self.level_iq = 100
        self.level_magic = 100
        self.money = money
