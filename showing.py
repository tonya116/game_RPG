from tkinter import *

WIDTH = 640
HEIGHT = 480

class Entity:

    def __init__(self, age, name, race, health, force, stamina, iq, magic, money):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=WIDTH, height=HEIGHT, bg='black')
        self.canvas.pack()
        self.color = "green"
        self.x = 100
        self.y = 100
        self.rect_id = self.canvas.create_rectangle(self.x, self.y, self.x + 10, self.y + 10, fill=self.color)


        self.age = age
        self.name = name
        self.race = race
        self.health = health
        self.force = force


    def damage(self, damage):
        self.health -= damage

    def regeneration(self):
        if self.level_health <= self.health-10:
            self.level_magic -= self.level_magic/2
            self.level_health += int(0.1 * self.health)

    def tick(self):
        self.root.after(50, self.tick)

    def move(self):


        self.root.update()
        
        self.root.bind('<Up>', lambda event: self.canvas.move(self.rect_id, 0, -10))
        self.root.bind('<Down>', lambda event: self.canvas.move(self.rect_id, 0, 10))
        self.root.bind('<Left>', lambda event: self.canvas.move(self.rect_id, -10, 0))
        self.root.bind('<Right>', lambda event: self.canvas.move(self.rect_id, 10, 0))
        self.root.mainloop()
