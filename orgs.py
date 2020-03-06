# -*- coding: utf-8 -*-
import showing as sh
from random import randrange as rndt
import portal as prtl
import spike_pillar as sp
import barrier
import hero

WIDTH = 640
HEIGHT = 480

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
        self.rect_id = sh.canvas.canvas.create_rectangle(self.x, self.y, self.x + 10, self.y + 10, fill=self.color)
        self.direction = ""

    def coords(self):
        self.coordinates = sh.canvas.canvas.coords(self.rect_id)
        sh.canvas.root.after(10,self.coords)


    def damage(self, damage):  #урон
        self.health -= damage
        if self.health < 1:
            print("death")
            death()



    def move_org(self):  # движение
        if hero.hero.coordinates[0] < self.coordinates[0]:
            sh.canvas.canvas.move(self.rect_id, -10, 0)
        if hero.hero.coordinates[1] < self.coordinates[1]:
            sh.canvas.canvas.move(self.rect_id, 0, -10)

        if hero.hero.coordinates[0] > self.coordinates[0]:
            sh.canvas.canvas.move(self.rect_id, 10, 0)
        if hero.hero.coordinates[1] > self.coordinates[1]:
            sh.canvas.canvas.move(self.rect_id, 0, 10)


        sh.canvas.root.after(500, self.move_org)
        #sh.canvas.canvas.move(self.rect_id, 0, 10))
        #sh.canvas.canvas.move(self.rect_id, -10, 0))
        #sh.canvas.canvas.move(self.rect_id, 10, 0))



    def checker_collide(self):

        for i in range(1):

            if int(self.coordinates[0]) < 0:
                sh.canvas.canvas.move(self.rect_id, 10, 0)
            elif int(self.coordinates[1]) < 0:
                sh.canvas.canvas.move(self.rect_id, 0, 10)
            elif int(self.coordinates[2]) > WIDTH:
                sh.canvas.canvas.move(self.rect_id, -10, 0)
            elif int(self.coordinates[3]) > HEIGHT:
                sh.canvas.canvas.move(self.rect_id, 0, -10)


        for item in prtl.list_of_portals:
            if self.coordinates == item.coordinates:
                sh.canvas.canvas.move(self.rect_id, rndt(-50, 50, 10), rndt(-50, 50, 10))



        for item in barrier.list_of_barriers:


            #прикасание справа
            if self.coordinates[0] == item.coordinates[2] and self.coordinates[1] == item.coordinates[1]:
                self.direction = "right"

            if self.coordinates == item.coordinates and self.direction == "right":

                sh.canvas.canvas.move(self.rect_id, 10, 0)
            #прикасание снизу
            if self.coordinates[0] == item.coordinates[0] and self.coordinates[1] == item.coordinates[3]:
                self.direction = "down"

            if self.coordinates == item.coordinates and self.direction == "down":

                sh.canvas.canvas.move(self.rect_id, 0, 10)
            #прикасание слева
            if self.coordinates[1] == item.coordinates[1] and self.coordinates[2] == item.coordinates[0]:
                self.direction = "left"

            if self.coordinates == item.coordinates and self.direction == "left":

                sh.canvas.canvas.move(self.rect_id, -10, 0)
            #прикасание сверху
            if self.coordinates[0] == item.coordinates[0] and self.coordinates[3] == item.coordinates[1]:
                self.direction = "up"

            if self.coordinates == item.coordinates and self.direction == "up":

                sh.canvas.canvas.move(self.rect_id, 0, -10)

        if self.coordinates == hero.hero.coordinates:
            hero.hero.damage(self.force)




        for item in sp.list_of_pillares:
            #укалывание справа
            if self.coordinates[0] == item.coordinates[2] and self.coordinates[1] == item.coordinates[1] :
                self.damage(item.force)
                sh.canvas.canvas.move(self.rect_id, 10, 0)
            #укалывание снизу
            elif self.coordinates[0] == item.coordinates[0] and self.coordinates[1] == item.coordinates[3] :
                self.damage(item.force)
                sh.canvas.canvas.move(self.rect_id, 0, 10)
            #укалывание слева
            elif self.coordinates[1] == item.coordinates[1] and self.coordinates[2] == item.coordinates[0] :
                self.damage(item.force)
                sh.canvas.canvas.move(self.rect_id, -10, 0)
            #укалывание сверху
            elif self.coordinates[0] == item.coordinates[0] and self.coordinates[3] == item.coordinates[1] :
                self.damage(item.force)
                sh.canvas.canvas.move(self.rect_id, 0, -10)



        sh.canvas.root.after(30, self.checker_collide)



list_of_orgs = []

for org in range(1):
    temp = Orgs("org" + str(org), "org", 100, 10, rndt(0, 640, 10), rndt(0, 480, 10))
    temp.coords()
    temp.move_org()
    temp.checker_collide()
    list_of_orgs.append(temp)
