# -*- coding: utf-8 -*-
from random import randrange as rndt


import showing as sh
import spike_pillar as sp
import portal as prtl
import barrier
import orgs
import hero
import interaction2 as inter



WIDTH = 640
HEIGHT = 480

list_of_all = []


def main():
    q = 0
    list_of_all.append(hero.hero)
    for i in orgs.list_of_orgs:
        list_of_all.append(i)

    for i in barrier.list_of_barriers:
        list_of_all.append(i)

    for i in prtl.list_of_portals:
        list_of_all.append(i)

    for i in sp.list_of_pillares:
        list_of_all.append(i)

    

    for i in list_of_all:
        for j in list_of_all:
            q += 1
            interaction = inter.Checker_collide(i, j)
            interaction.interaction()


    sh.canvas.root.mainloop()

main()
