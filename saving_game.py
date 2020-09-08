# -*- coding: utf-8 -*-
from config import *
from random import randrange as rndt

import apple
import showing as sh
import spike_pillar as sp
import portal as prtl
import barrier
import orgs
import hero
import interaction2 as inter

def saveIt():
    file = open("saves/1.txt", "w")
    file.write(str(hero.hero.name) + ",")
    file.write(str(hero.hero.race) + ",")
    file.write(str(hero.hero.health) + ",")
    file.write(str(hero.hero.force) + ",")
    file.write(str(hero.hero.level_magic) + ",")
    file.write(str(hero.hero.coordinates[0]) + ",")
    file.write(str(hero.hero.coordinates[1]))
    file.close()
