# -*- coding: utf-8 -*-
import showing as sh
import hero
import portal as prtl
import orgs

from random import randrange as rndt

WIDTH = 640
HEIGHT = 480

def checker_collide():
    for entity in orgs.list_of_orgs:
        if int(entity.coordinates[0]) < 0:
            sh.canvas.canvas.move(entity.rect_id, 10, 0)
        elif int(entity.coordinates[1]) < 0:
            sh.canvas.canvas.move(entity.rect_id, 0, 10)
        elif int(entity.coordinates[2]) > WIDTH:
            sh.canvas.canvas.move(entity.rect_id, -10, 0)
        elif int(entity.coordinates[3]) > HEIGHT:
            sh.canvas.canvas.move(entity.rect_id, 0, -10)

    for entity in prtl.list_of_portals:
        if int(entity.coordinates[0]) < 0:
            sh.canvas.canvas.move(entity.rect_id, 10, 0)
        elif int(entity.coordinates[1]) < 0:
            sh.canvas.canvas.move(entity.rect_id, 0, 10)
        elif int(entity.coordinates[2]) > WIDTH:
            sh.canvas.canvas.move(entity.rect_id, -10, 0)
        elif int(entity.coordinates[3]) > HEIGHT:
            sh.canvas.canvas.move(entity.rect_id, 0, -10)


    if int(hero.hero.coordinates[0]) < 0:
        sh.canvas.canvas.move(hero.hero.rect_id, 10, 0)
    elif int(hero.hero.coordinates[1]) < 0:
        sh.canvas.canvas.move(hero.hero.rect_id, 0, 10)
    elif int(hero.hero.coordinates[2]) > WIDTH:
        sh.canvas.canvas.move(hero.hero.rect_id, -10, 0)
    elif int(hero.hero.coordinates[3]) > HEIGHT:
        sh.canvas.canvas.move(hero.hero.rect_id, 0, -10)
    sh.canvas.root.after(50, checker_collide)

def damaging():
    for entity in orgs.list_of_orgs:
        if hero.hero.coordinates == entity.coordinates:
            hero.hero.damage(entity.force)
    sh.canvas.root.after(50, damaging)

def portal_checker():
    for item in prtl.list_of_portals:
        for entity in orgs.list_of_orgs:
            if entity.coordinates == item.coordinates:
                sh.canvas.canvas.move(entity.rect_id, rndt(-50, 50, 10), rndt(-50, 50, 10))
    sh.canvas.root.after(50, portal_checker)


def fight():

    for entity in orgs.list_of_orgs:
        if hero.hero.coordinates[0] == entity.coordinates[2] and hero.hero.coordinates[1] == entity.coordinates[1]:
            entity.damage(hero.hero.force)
        if hero.hero.coordinates[0] == entity.coordinates[0] and hero.hero.coordinates[1] == entity.coordinates[3]:
            entity.damage(hero.hero.force)
        if hero.hero.coordinates[1] == entity.coordinates[1] and hero.hero.coordinates[2] == entity.coordinates[0]:
            entity.damage(hero.hero.force)
        if hero.hero.coordinates[0] == entity.coordinates[0] and hero.hero.coordinates[3] == entity.coordinates[1]:
            entity.damage(hero.hero.force)


sh.canvas.root.bind('<space>', lambda event: fight())

checker_collide()

damaging()
portal_checker()
