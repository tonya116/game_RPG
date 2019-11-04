from tkinter import *


class Showing:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x500")
        self.canvas = Canvas(self.root, width = 500, height = 500, bg = 'black')
        self.canvas.pack()
    def to_draw(self):
        self.root.mainloop()

    def show(self):
        self.object =  self.canvas.create_rectangle(10,10,20,20, fill = "green")
        self.to_draw()
