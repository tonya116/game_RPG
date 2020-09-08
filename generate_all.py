# -*- coding: utf-8 -*-

from config import *
from random import randrange as rndt
import apple as ap
import spike_pillar as sp
import portal as prtl
import orgs


list_of_apples = []
list_of_portals = []
list_of_pillares = []
list_of_orgs = []
list_of_all = []

def regenerate():

    global list_of_apples, list_of_portals, list_of_pillares, list_of_orgs, hero

    if  len(list_of_apples) != 0:
        list_of_all.remove(list_of_apples)
        for apple in list_of_apples:
            list_of_apples.remove(apple)
            apple.death()

    if  len(list_of_portals) != 0:
        list_of_all.remove(list_of_portals)
        for portal in list_of_portals:
            list_of_portals.remove(portal)
            portal.death()

    if len(list_of_pillares) != 0:
        list_of_all.remove(list_of_pillares)
        for pillar in list_of_pillares:
            list_of_pillares.remove(pillar)
            pillar.death()

    if len(list_of_orgs) != 0:
        list_of_all.remove(list_of_orgs)
        for org in list_of_orgs:
            list_of_orgs.remove(org)
            org.death()

    for apple in range(count_of_apples):
        temp = ap.Apple("apple" + str(apple), "apple", 25, rndt(0, WIDTH, step), rndt(0, HEIGHT, step))
        temp.coords()
        list_of_apples.append(temp)

    for portal in range(count_of_portals):
        temp = prtl.Portal("p" + str(portal), "portal", 1, 0, rndt(0, WIDTH, step), rndt(0, HEIGHT, step))
        temp.coords()
        list_of_portals.append(temp)

    for pillar in range(count_of_pillares):
        temp = sp.SpikePillar("sp" + str(pillar), "spike_pillar", 1, 5, rndt(0, WIDTH, step), rndt(0, HEIGHT, step))
        temp.coords()
        list_of_pillares.append(temp)

    for org in range(count_of_orgs):
        temp = orgs.Orgs("org" + str(org), "org", 100, 1, rndt(0, WIDTH, step), rndt(0, HEIGHT, step))
        temp.coords()
        temp.move_org()

        list_of_orgs.append(temp)

    list_of_all.append(list_of_apples)
    list_of_all.append(list_of_portals)
    list_of_all.append(list_of_pillares)
    list_of_all.append(list_of_orgs)
