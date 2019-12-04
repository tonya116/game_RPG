## -*- coding: utf-8 -*-
from tkinter import *

WIDTH = 640
HEIGHT = 480

class Entity:
    """ класс кубика на экране"""

    def __init__(self, age, name, race, health, force, stamina, iq, magic, money):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=WIDTH, height=HEIGHT, bg='black')
        self.canvas.pack()
        self.x = 100
        self.y = 100
        self.age = age
        self.name = name
        self.race = race
        self.health = health
        self.force = force
        if race == "Human":
            self.color = "green"
        self.rect_id = self.canvas.create_rectangle(self.x, self.y, self.x + 10, self.y + 10, fill=self.color)


    def damage(self, damage):  #урон
        self.health -= damage

    def regeneration(self):  #регенерация
        if self.level_health <= self.health-10:
            self.level_magic -= self.level_magic/2
            self.level_health += int(0.1 * self.health)


    def move(self):  # движение
        self.root.bind('<w>', lambda event: self.canvas.move(self.rect_id, 0, -10))
        self.root.bind('<s>', lambda event: self.canvas.move(self.rect_id, 0, 10))
        self.root.bind('<a>', lambda event: self.canvas.move(self.rect_id, -10, 0))
        self.root.bind('<d>', lambda event: self.canvas.move(self.rect_id, 10, 0))
        self.root.mainloop()
