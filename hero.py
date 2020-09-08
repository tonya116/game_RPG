# -*- coding: utf-8 -*-
from config import *

import showing as sh
from random import randrange as rndt
import orgs
import interaction2 as inter
#import server as s






class Hero:
    """
    этот класс связан со всем, что связано с героем
    """
    def __init__(self, name, race, health, force, level_magic, x, y):
        self.x = x
        self.y = y
        self.name = name
        self.health = health
        self.race = race
        self.force = force
        self.level_magic = level_magic
        self.color = "green"
        self.rect_id = sh.Entity(x, y, self.color)
        self.name_label = sh.canvas.canvas.create_text(HEIGHT/5*1, 500,
                                text = "name = " + str(self.name), fill="white")
        self.health_label = sh.canvas.canvas.create_text(HEIGHT/5*2, 500,
                                text = "health = " + str(self.health) + "%", fill="white")
        self.race_label = sh.canvas.canvas.create_text(HEIGHT/5*3, 500,
                                text = "race = " + str(self.race), fill="white")
        self.force_label = sh.canvas.canvas.create_text(HEIGHT/5*4, 500,
                                text = "force = " + str(self.force), fill="white")
        self.level_magic_label = sh.canvas.canvas.create_text(HEIGHT/5*5, 500,
                                text = "level_magic = " + str(self.level_magic), fill="white")
        self.mapping = {"s": (0, step), "w": (0, -step),
                        "a": (-step, 0), "d": (step, 0) }

        self.vector = self.mapping["d"]



    def coords(self):
        self.coordinates = self.rect_id.coords()
        self.x1 = self.coordinates[0]
        self.y1 = self.coordinates[1]
        self.x2 = self.coordinates[2]
        self.y2 = self.coordinates[3]


    def damage(self, damage):  #урон
        self.health -= damage
        sh.canvas.canvas.itemconfig(self.health_label,
                    text = "health = " + str(self.health) + "%")
        #self.health_label.config(text = "health = " + str(int(self.health)) + "%")
        if self.health <= 0:
            self.death()

    def death(self):
        sh.canvas.canvas.itemconfig(self.health_label,
                            text = "You are dead")
        sh.canvas.canvas.delete(self.rect_id.rect_id)
        del self




    def key_press(self, event):

        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]
            self.v_x, self.v_y = self.vector
            self.coords()
            self.move()

        if event.keysym == "space":
            inter.inter.orgs(self, orgs.list_of_orgs)




    def move(self):

        self.coords()

        inter.inter.apple(self)
        inter.inter.barrier(self)
        inter.inter.portal(self)
        inter.inter.pillares(self)

    def move_hero_bind(self):

        sh.canvas.root.bind("<KeyPress>", self.key_press)

    def healing(self, health):

        if self.health + health >= 100:
            self.health = 100
        else:
            self.health += health
        sh.canvas.canvas.itemconfig(self.health_label,
                            text = "health = " + str(self.health) + "%")
        #self.health_label.config(text = "health = " + str(int(self.health)) + "%")

    def regeneration(self):  #регенерация

        if self.health <= 20:
            self.level_magic -= self.level_magic/2
            sh.canvas.canvas.itemconfig(self.level_magic_label,
                    text = "level_magic = " + str(int(self.level_magic)) + "%")
            self.health *= 1.5
            sh.canvas.canvas.itemconfig(self.health_label,
                    text = "health = " + str(int(self.health)) + "%")

        sh.canvas.canvas.after(3000, self.regeneration)

    def regeneration_magic(self):

        if self.level_magic < 100 and self.level_magic >= 0:
            self.level_magic += 1
            sh.canvas.canvas.itemconfig(self.level_magic_label,
                    text = "level_magic = " + str(int(self.level_magic)) + "%")

        sh.canvas.canvas.after(1000, self.regeneration_magic)



hero = Hero(name_of_hero, "Hero" , 100, 50, 100, rndt(0, HEIGHT, step) ,rndt(0, HEIGHT, step))
hero.coords()
hero.move_hero_bind()
hero.regeneration_magic()
hero.regeneration()
