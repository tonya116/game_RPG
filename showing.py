from tkinter import *

WIDTH = 640
HEIGHT = 480




class Entity():

    def __init__(self, age, name, race, health, force, stamina, iq, magic, money):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=WIDTH, height=HEIGHT, bg='black')
        self.canvas.pack()
        self.color = "green"
        self.x = 100
        self.y = 100
        self.rect_id = self.canvas.create_rectangle(self.x, self.y, self.x + 10, self.y + 10, fill=self.color)
        self.root.mainloop()
        self.age = age
        self.name = name
        self.race = race
        self.health = health
        self.force = force
        self.stamina = stamina
        self.iq = iq
        self.magic = magic
        self.level_health = self.health
        self.level_force = 100
        self.level_stamina = 100
        self.level_iq = 100
        self.level_magic = 100
        self.money = money

    def damage(self, damage):
        self.level_health -= damage


    def regeneration(self):
        if self.level_health <= self.health-10:
            self.level_magic -= self.level_magic/2
            self.level_health += int(0.1 * self.health)

    def tick(self):
        after(50, tick)


#obj = Entity(20, "Den", "Human", 100, 1, 1, 1, 1, 100)
