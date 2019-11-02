import humans
import orgs
import tkinter
from tkinter import *



hero = humans.Humans(20, "Den", "Human", 100, 1, 1, 1, 1, 100 )



hero.damage(30)
hero.regeniration()
hero.regeniration()
print(hero.level_health)
print(hero.level_magic)


root = Tk()
root.geometry("500x500")

canvas = Canvas(root, width = 500, height = 500, bg = 'black')



canvas.pack()
root.mainloop()
