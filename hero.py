# -*- coding: utf-8 -*-
import showing as sh
from random import randrange as rndt

import portal as prtl
import spike_pillar as sp
import barrier



WIDTH = 640
HEIGHT = 480

class Hero:
    """
    этот класс связан со всем, что связано с героем
    """
    def __init__(self, name, race, health, force, x, y):
        self.x = x
        self.y = y
        self.word = 0
        self.health = health
        self.race = race
        self.force = force
        self.color = "green"
        self.direction = ""
        self.rect_id = sh.Entity(x, y, self.color)
        self.health_label = sh.Label(sh.canvas.root, text = "health = " + str(self.health) + "%")
        self.mapping = {"s": (0, 10), "w": (0, -10),
                        "a": (-10, 0), "d": (10, 0) }

        self.vector = self.mapping["d"]
        self.health_label.grid()


    def coords(self):
        self.coordinates = self.rect_id.coords()
        sh.canvas.root.after(10, self.coords)

    def check_collide_box(self):

        if int(self.coordinates[0]) < 0:
            sh.canvas.canvas.move(self.rect_id, 10, 0)
        elif int(self.coordinates[1]) < 0:
            sh.canvas.canvas.move(self.rect_id, 0, 10)
        elif int(self.coordinates[2]) > WIDTH:
            sh.canvas.canvas.move(self.rect_id, -10, 0)
        elif int(self.coordinates[3]) > HEIGHT:
            sh.canvas.canvas.move(self.rect_id, 0, -10)

        sh.canvas.root.after(10,self.check_collide_box)


    def damage(self, damage):  #урон
        self.health -= damage
        self.health_label.config(text = "health = " + str(self.health) + "%")
        if self.health < 1:
            self.health_label.destroy()
            death()



    def change_direction(self, event):
        """ Изменяет направление движения Героя """

        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]
            print(event.keysym)
            print(self.vector)
            self.move()

    def move(self):

        #sh.canvas.canvas.move(self.rect_id.rect_id, self.vector[0], self.vector[1])
        self.coords()

        for item in barrier.list_of_barriers:

            if (self.coordinates[0] == item.coordinates[2] and self.coordinates[1] == item.coordinates[1] and self.vector[0] == -10 and self.vector[1] == 0) or (self.coordinates[0] == item.coordinates[0] and self.coordinates[1] == item.coordinates[3] and self.vector[0] == 0 and self.vector[1] == -10) or (self.coordinates[1] == item.coordinates[1] and self.coordinates[2] == item.coordinates[0] and self.vector[0] == 10 and self.vector[1] == 0) or (self.coordinates[0] == item.coordinates[0] and self.coordinates[3] == item.coordinates[1] and self.vector[0] == 0 and self.vector[1] == 10):
                pass
            else:
                self.word += 1

        print(self.word, len(barrier.list_of_barriers))

        if self.word == len(barrier.list_of_barriers):
            sh.canvas.canvas.move(self.rect_id.rect_id, self.vector[0], self.vector[1])



        self.word = 0


    def move_hero_bind(self):

        sh.canvas.root.bind("<KeyPress>", self.change_direction)

    def checker_collide(self):

        for item in prtl.list_of_portals:
            if self.coordinates == item.coordinates:
                sh.canvas.canvas.move(self.rect_id.rect_id, rndt(-50, 50, 10), rndt(-50, 50, 10))




        for item in sp.list_of_pillares:
            #укалывание справа
            if self.coordinates[0] == item.coordinates[2] and self.coordinates[1] == item.coordinates[1] :
                self.damage(item.force)
                sh.canvas.canvas.move(self.rect_id.rect_id, 10, 0)
            #укалывание снизу
            elif self.coordinates[0] == item.coordinates[0] and self.coordinates[1] == item.coordinates[3] :
                self.damage(item.force)
                sh.canvas.canvas.move(self.rect_id.rect_id, 0, 10)
            #укалывание слева
            elif self.coordinates[1] == item.coordinates[1] and self.coordinates[2] == item.coordinates[0] :
                self.damage(item.force)
                sh.canvas.canvas.move(self.rect_id.rect_id, -10, 0)
            #укалывание сверху
            elif self.coordinates[0] == item.coordinates[0] and self.coordinates[3] == item.coordinates[1] :
                self.damage(item.force)
                sh.canvas.canvas.move(self.rect_id.rect_id, 0, -10)



        sh.canvas.root.after(30, self.checker_collide)







hero = Hero("Den", "Hero", 100, 50, rndt(0, 640, 10),rndt(0, 480, 10))


hero.coords()
hero.move_hero_bind()


hero.check_collide_box()
hero.checker_collide()





def death():
    global hero
    sh.canvas.canvas.delete(hero.rect_id.rect_id)
    death_label = sh.Label(sh.canvas.root, text = "You dead")
    death_label.grid()
    del hero














    #def regeneration(self):  #регенерация
    #    if self.level_health <= self.health-10:
    #        self.level_magic -= self.level_magic/2
    #        self.level_health += int(0.1 * self.health)
